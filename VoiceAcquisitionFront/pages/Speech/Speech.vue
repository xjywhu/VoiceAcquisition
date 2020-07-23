<template>
    <view>
		<uni-card 
			title="阅读卡片" 
			mode="basic" 
			:is-shadow="true" 
			note="金额:100"
			:threshold="'阈值:'+threshold"
		>
		
<!-- 		<view class="uni-list">
			<view class="uni-list-cell" hover-class="uni-list-cell-hover" v-for="(item,index) in sentence" :key="index">
			item
			</view>
		</view> -->
		
		{{sentence}}
		</uni-card>
        	<aui-dialog 
        	    ref="dialog"
        	    :title="auiDialog.title"
        	    :msg="auiDialog.msg"
        	    :btns="auiDialog.btns"
        	    :mask="auiDialog.mask"
        	    :maskTapClose="auiDialog.maskTapClose"
        	    :items="auiDialog.items"
        	    :theme="auiDialog.theme"
        	    @callback="dialogCallback"
        	></aui-dialog>
		<page-head :title="title"></page-head>
        <view class="uni-padding-wrap">
            <block v-if="!recording && !playing && !hasRecord">
                <view class="page-body-time">
                    <text class="time-big">{{formatedRecordTime}}</text>
                </view>
                <view class="page-body-buttons">
                    <view class="page-body-button"></view>
                    <view class="page-body-button" @click="startRecord">
                        <image src="../../static/speech/record.png"></image>
                    </view>
                    <view class="page-body-button"></view>
                </view>
            </block>
            <block v-if="recording === true">
                <view class="page-body-time">
                    <text class="time-big">{{formatedRecordTime}}</text>
                </view>
                <view class="page-body-buttons">
                    <view class="page-body-button"></view>
                    <view class="page-body-button" @click="stopRecord">
                        <view class="button-stop-record"></view>
                    </view>
                    <view class="page-body-button"></view>
                </view>
            </block>
            <block v-if="hasRecord === true && playing === false">
                <view class="page-body-time">
                    <text class="time-big">{{formatedPlayTime}}</text>
                    <text class="time-small">{{formatedRecordTime}}</text>
                </view>
                <view class="page-body-buttons">
                    <view class="page-body-button" @click="playVoice">
                        <image src="../../static/speech/play.png"></image>
                    </view>
                    <view class="page-body-button" @click="clear">
                        <image src="../../static/speech/trash.png"></image>
                    </view>
					<view class="page-body-button" @click="upload">
					    <image src="../../static/speech/upload.png"></image>
					</view>					
                </view>
            </block>
            <block v-if="hasRecord === true && playing === true">
                <view class="page-body-time">
                    <text class="time-big">{{formatedPlayTime}}</text>
                    <text class="time-small">{{formatedRecordTime}}</text>
                </view>
                <view class="page-body-buttons">
                    <view class="page-body-button" @click="stopVoice">
                        <image src="../../static/speech/stop.png"></image>
                    </view>
                    <view class="page-body-button" @click="clear">
                        <image src="../../static/speech/trash.png"></image>
                    </view>
                </view>
            </block>
        </view>
    </view>
</template>
<script>
	// #ifdef APP-PLUS
	import permision from "@/common/permission.js"
	// #endif
	import {aui} from '@/common/aui/js/aui.js';
	import auiDialog from '@/components/aui-dialog/aui-dialog.vue';
    var util = require('../../common/util.js')
    var playTimeInterval = null;
    var recordTimeInterval = null;
    var recorderManager = null;
    var music = null;
    export default {
		components: {
			auiDialog
		},
        data() {
            return {
				cid:"",
				sentence:"",
				voice_text:"",
				sentence_list:[],
				voice_list:[],
				threshold:"",
                title: 'start/stopRecord、play/stopVoice',
                recording: false, //录音中
                playing: false, //播放中
                hasRecord: false, //是否有了一个
                tempFilePath: '',
                recordTime: 0,
                playTime: 0,
                formatedRecordTime: '00:00:00', //录音的总时间
                formatedPlayTime: '00:00:00' ,//播放录音的当前时间
				auiDialog: {
					title: '',
					msg: '',
					btns: [{name: '确定'}],
					mask: true,
					maskTapClose: true,
					items: [],
					theme: 1,
				}
            }
        },
        onUnload: function() {
            this.end(); 
        },
        onLoad: function(e) {
			this.cid = e.cid;
			this.sentence = e.sentence; 
			this.threshold = e.threshold;
			console.log(e);
            music = uni.createInnerAudioContext();
            music.onEnded(() => {
                clearInterval(playTimeInterval)
                var playTime = 0
                console.log('play voice finished')
                this.playing = false;
                this.formatedPlayTime = util.formatTime(playTime);
                this.playTime = playTime;
            });
            recorderManager = uni.getRecorderManager();
            recorderManager.onStart(() => {
                console.log('recorder start');
                this.recording = true;
                recordTimeInterval = setInterval(() => {
                    this.recordTime += 1;
                    this.formatedRecordTime = util.formatTime(this.recordTime);
                }, 1000)
            });
            recorderManager.onStop((res) => {
                console.log('on stop');
                music.src = res.tempFilePath;
				this.tempFilePath  = res.tempFilePath;
                this.hasRecord = true;
                this.recording = false;
				console.log(res.tempFilePath);
            });
            recorderManager.onError(() => {
                console.log('recorder onError');
            });
        },
        methods: {
			highLight(content, indexs) {
				var res = [];
				for(var i=0;i<content.length;i++)
				{
					if(indexs[i]==1 || indexs[i]==2 || indexs[i]==-1)
					{
						res.push({
							type: 1,
							text: content[i],
						});
					}else 
					{
						res.push({
							type: 0,
							text: content[i],
						});
					}
				}
			  return res;
			},
			//dialog弹窗底部按钮回调
			dialogCallback(e){
				var _this = this;
				//console.log(e);             
				if(_this.$refs.dialog.getVal().length > 0)
				{ //prompt输入框——点击确定时弹出输入内容
					_this.auiDialog.title = '提示';
					_this.$refs.dialog.getVal().forEach(function(item, index){
					_this.auiDialog.msg += '<div style="display: flex;">' + item.label + '：' + item.value + '</div>';
					});
					_this.auiDialog.btns = [{name: '确定', color: '#197DE0'}];
					_this.auiDialog.items = [];
					_this.auiDialog.theme = 1;
					_this.$refs.dialog.show();
				}
			},
			alert(theme,title,msg){
				var _this = this;
				_this.auiDialog.title = title;
				_this.auiDialog.msg = msg;
				_this.auiDialog.btns = [{name: '确定', color: '#197DE0'}];
				// _this.auiDialog.items = [{label: '原始文本：', type: 'text', value: this.sentence},
				// {label: '录音文本：', type: 'text', value: this.voice_text}
				// ];
				_this.auiDialog.items = [{label: '原始文本：', type: 'text', value: this.sentence_list},
				{label: '录音文本：', type: 'text', value: this.voice_list}
				];
				console.log(_this.auiDialog.items);
				_this.auiDialog.theme = theme;
				_this.$refs.dialog.show();
			},
            async startRecord() { //开始录音
                // #ifdef APP-PLUS
                let status = await this.checkPermission();
                if (status !== 1) {
                    return;
                }
                // #endif
                // TODO ios 在没有请求过权限之前无法得知是否有相关权限，这种状态下需要直接调用录音，但没有状态或回调判断用户拒绝
                recorderManager.start({
                    format: 'mp3'
                });
            },
            stopRecord() { //停止录音
                recorderManager.stop();
                clearInterval(recordTimeInterval);
            },
            playVoice() {
                console.log('play voice');
                this.playing = true;
                playTimeInterval = setInterval(() => {
                    this.playTime += 1;
                    this.formatedPlayTime = util.formatTime(this.playTime);
                }, 1000)
                music.play();
            },
            stopVoice() {
                clearInterval(playTimeInterval)
                this.playing = false;
                this.formatedPlayTime = util.formatTime(0);
                this.playTime = 0;
                music.stop();
            },
            end() {
                music.stop();
                recorderManager.stop();
                clearInterval(recordTimeInterval)
                clearInterval(playTimeInterval);
                this.recording = false, this.playing = false, this.hasRecord = false;
                this.playTime = 0, this.recordTime = 0;
                this.formatedRecordTime = "00:00:00", this.formatedRecordTime = "00:00:00";
            },
			upload() {
				wx.uploadFile({
					url: global.base_url+"voices_info/"+this.cid+"/"+global.user_data.jwt,
					filePath: this.tempFilePath, 
					name:"voice_file",
					header: {
						"Content-Type": "multipart/form-data",
					},
					formData:{
						name:"voice_file",
					},
					success: res => {
						//"{"StatusCode":"fail","failType":"otherFail","failReason":"匹配度未达到阈值","data":{"voice_text":"今天怎么样？","context_text":"今天天气怎么样","a":[0,1,0,1,0,0,0],"b":[0,0,0,0,0,1],"rate":0.5714285714285714,"user":{"wx_number":"oVCRb5DxhSYL45xLJDmMxErDPyYY","nickName":"小鱼儿","score":356,"native_place":"Henan","image":"https://wx.qlogo.cn/mmopen/vi_32/iaMia0X5uB8LBWBibGzaeknkjouNxN08muhDVpiaVU4cOASkZrZEkibUiaep6MMs8eX0rHBmZQK5qPiaMHXEamWlVP3jQ/132","sex":"男","task_times":44,"success_times":5}}}"
						console.log(res);
						var js = JSON.parse(res.data);
						var rate = js["data"]["rate"];
						var score = js["data"]["user"]["score"];
						global.user_data.score = score;
						var total_times = js["data"]["user"]["task_times"];
						var success_times = js["data"]["user"]["success_times"];
						global.user_data.accuracy = Math.round(success_times*100/total_times);
						this.voice_text = js["data"]["voice_text"];
						this.sentence_list = this.highLight(this.sentence,js.data.a);
						this.voice_list = this.highLight(this.voice_text,js.data.b);
						console.log(js.data.a);
						console.log(js.data.b);
						// console.log(this.voice_list);
						if(js["StatusCode"]=="fail")
						{
							this.alert(1,"上传失败","准确率:"+rate*100+"%");
						}else{
							this.alert(1,"上传成功","准确率:"+rate*100+"%");
						}
					},
					fail: res=>{
						console.log(res)
						console.log("上传失败")
					},
				});
				this.end();
			},
            clear() {
                this.end();
            }
            // #ifdef APP-PLUS
            ,
            async checkPermission() {
                let status = permision.isIOS ? await permision.requestIOS('record') :
                    await permision.requestAndroid('android.permission.RECORD_AUDIO');
                if (status === null || status === 1) {
                    status = 1;
                } else if (status === 2) {
                    uni.showModal({
                        content: "系统麦克风已关闭",
                        confirmText: "确定",
                        showCancel: false,
                        success: function(res) {
                        }
                    })
                } else {
                    uni.showModal({
                        content: "需要麦克风权限",
                        confirmText: "设置",
                        success: function(res) {
                            if (res.confirm) {
                                permision.gotoAppSetting();
                            }
                        }
                    })
                }
                return status;
            }
            // #endif
        }
    }
</script>

<style>
    image {
        width: 150rpx;
        height: 150rpx;
    }
    .page-body-wrapper {
        justify-content: space-between;
        flex-grow: 1;
        margin-bottom: 300rpx;
    }
    .page-body-time {
        display: flex;
        flex-direction: column;
        align-items: center;
    }
    .time-big {
        font-size: 60rpx;
        margin: 20rpx;
    }
    .time-small {
        font-size: 30rpx;
    }
    .page-body-buttons {
        margin-top: 60rpx;
        display: flex;
        justify-content: space-around;
    }
    .page-body-button {
        width: 250rpx;
        text-align: center;
    }
    .button-stop-record {
        width: 110rpx;
        height: 110rpx;
        border: 20rpx solid #fff;
        background-color: #f55c23;
        border-radius: 130rpx;
        margin: 0 auto;
    }
</style>