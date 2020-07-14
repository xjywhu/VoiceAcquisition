<template>
	<view>
		<!-- 标题卡片模式 -->
		<uni-card 
		    title="阅读卡片" 
		    mode="basic" 
		    :is-shadow="true" 
		    note="Tips"
		>
		{{sentence}}
		</uni-card>
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
				cid:"",
				sentence:""
			}
		},
		onLoad:function(e){
			console.log(e);
			this.cid = e.cid;
			this.sentence = e.sentence; 
			recorderManager.onStop(function(res) {
				console.log(res.tempFilePath)
				wx.uploadFile({
					url: global.base_url+"voices_info/"+e.cid+"/"+global.user_data.wx_number,
					filePath: res.tempFilePath,
					name:"voice_file",
					header: {
						"Content-Type": "multipart/form-data",
					},
					formData:{
						name:"voice_file",
					},
					success: res => {
						console.log(res)
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
