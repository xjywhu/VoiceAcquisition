<template>
	<view>
		<button @tap="startRecord">开始录音</button>
		<button @tap="endRecord">停止录音</button>
		<button @tap="playVoice">播放录音</button>
	</view>
</template>

<script>
	const recorderManager = uni.getRecorderManager();
	const innerAudioContext = uni.createInnerAudioContext();
	innerAudioContext.autoplay = true;
	export default {
		data() {
			return {
			}
		},
		onLoad() {
			recorderManager.onStop(function(res) {
				console.log(res.tempFilePath)
				wx.uploadFile({
					url: "http://127.0.0.1:8000/api/v1/upload/",
					filePath: res.tempFilePath,
					name:"file",
					header: {
						"Content-Type": "multipart/form-data",
					},
					formData:{
						name:"hh",
					},
					success: res => {
						console.log(res)
					// let url = JSON.parse(res.data).data.url;
					// let size = JSON.parse(res.data).data.size;
							// let suffix = JSON.parse(res.data).data.ext;		
						},
						fail: res=>{
							console.log(res)
							console.log("上传失败")
						},
					})
				});
			},
			methods: {
				startRecord() {
					console.log('开始录音');
					recorderManager.start({
						sampleRate: 16000 ,// 必须设置是后台设置的参数，不然百度语音识别不了
						format:"mp3",
					});
				},
				endRecord() {
					console.log('录音结束');
					recorderManager.stop();
				},
				playVoice() {
					console.log('播放录音');
					if (this.voicePath) {
						innerAudioContext.src = this.voicePath;
						innerAudioContext.play();
					}
				}
			}
		}
</script>

<style>
</style>
