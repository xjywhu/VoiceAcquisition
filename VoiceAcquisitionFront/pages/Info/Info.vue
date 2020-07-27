<template>
	<view>
		<view class="top">
			<view class="center">
				<view class="center_top">
					<view class="center_img" @tap="toBaseInfo">
						<!-- 头像 -->
						<image class="user_head" :src="avatarUrl">头像</image>
						<!-- <image src="../../static/image/头像.jpg"></image> -->
						<!-- <open-data type="userAvatarUrl" class="user_head"></open-data> -->
					</view>
					<view class="center_info" @tap="toBaseInfo">
						<view class="center_name">{{trueName}}</view>
						<!-- <view class="center_phone">phone:{{phone}}</view> -->
						<view class="center_phone">基本信息</view>
						<text class="nickName">昵称:{{nickNames}}</text>
						<text class="sex">性别:{{sex}}</text>
						<text class="native">籍贯:{{native}}</text>
					</view>
				</view>
				<view class="center_down">
					<view class="center_rank" @tap="toNone">
						<image class="rank_icon" src="../../static/icon/排名.png"></image>
						<text class="rank_text">准确度:{{accuracy}}%</text>
					</view>
					<view class="center_score" @tap="toNone">
						<image class="rank_icon" src="../../static/icon/积分.png"></image>
						<text class="rank_text">积分:{{score}}</text>
					</view>
				</view>
			</view>
			<image src='https://6661-fatdown-wxapp-sg2p1-1300398887.tcb.qcloud.la/wave.gif?sign=045605c672f482a8c3d428abed669aa7&t=1570674356' mode='scaleToFill' class='gif-wave'></image>
		</view>
		<uni-list>
		    <uni-list-item title="我的任务" thumb="../../static/icon/我的任务.png"></uni-list-item>
		    <uni-list-item title="充值积分" thumb="../../static/icon/充值.png"></uni-list-item>
		    <uni-list-item title="积分提现" thumb="../../static/icon/提现.png"></uni-list-item>
		</uni-list>
	</view>
	
		
</template>

var _this;
<script>
	import uniListItem from '@/components/uni-list-item/uni-list-item.vue'
	export default {
		components:{
			uniListItem
		},
		data() {
			return {
				wx_number: 'unknown',
				nickNames: '匿名用户',
				avatarUrl: 'http://img2.imgtn.bdimg.com/it/u=2091711702,2468700162&fm=11&gp=0.jpg',//默认头像路径
				sex: '',
				age: '',
				gender: 0,
				native: '',
				show: '',
				hidden: '',
				score:'',
				accuracy:0,
			}
		},
		methods: {
			getAllClass: () => {
			    return new Promise((resolve, reject) => {
			        uni.request({
						url:global.base_url+"auto_login/"+global.user_data.jwt,
			            success: (res) => {
			                //store.commit('setAllClass', res.data);
							var statusCode = res.data.StatusCode
							var data = res.data.data
							global.user_data.avatarUrl = data.image
							global.user_data.native = data.native_place
							global.user_data.nickNames = data.nickName
							global.user_data.score = data.score
							global.user_data.wx_number = data.wx_number
							global.user_data.sex = data.sex
							global.user_data.accuracy = Math.round(data.success_times*100/data.task_times)
							global.isLogin = true
							console.log(global.isLogin);
							// 刷新jwt，需要这个功能吗？
							//global.user_data.jwt = data.newJWT 
							//console.log(data.newJWT)
							uni.setStorage({
								key:'JWT',
								data:global.user_data.jwt
							})
			            },
			            fail: (err) => {
			            }
			        });
			    })
			}
		},
		onShow:function(){
			// console.log("OnShow -------------------------------");
			let _self = this;
			_self.wx_number = global.user_data.wx_number;
			_self.nickNames = global.user_data.nickNames;
			_self.avatarUrl = global.user_data.avatarUrl;
			_self.sex = global.user_data.sex;
			_self.age = global.user_data.age;
			_self.gender = global.user_data.gender;
			_self.native = global.user_data.native;
			_self.show = global.user_data.show; 
			_self.hidden = global.user_data.hidden;
			_self.score = global.user_data.score;
			_self.accuracy = global.user_data.accuracy;
			console.log(global.isLogin);
			// uni.showLoading({
			// 	title:"加载中....",
			// 	mask: true,
			// })
		},
		onLoad:function(option) {
			uni.showLoading({
				title:"加载中....",
				mask: true,
			})
			return new Promise(resolve=>{
				setTimeout(()=>{
					let _self = this;
					_self.wx_number = global.user_data.wx_number;
					_self.nickNames = global.user_data.nickNames;
					_self.avatarUrl = global.user_data.avatarUrl;
					_self.sex = global.user_data.sex;
					_self.age = global.user_data.age;
					_self.gender = global.user_data.gender;
					_self.native = global.user_data.native;
					_self.show = global.user_data.show; 
					_self.hidden = global.user_data.hidden;
					_self.score = global.user_data.score;
					_self.accuracy = global.user_data.accuracy;
					console.log(global.isLogin);
					if(!global.isLogin){
						console.log('未登录...');
						//showUniPop();
						uni.showModal({
							title:'提醒',
							content:'请登录',
							success:function(res){
								if(res.confirm){
									uni.navigateTo({
										url:'../Login/Login'
									});
								}
							},
						});
					}
					uni.hideLoading();
					resolve();
				},2000)
			})
			
			
			// console.log("OnLoad");
			// try {
			//     const value = uni.getStorageSync('JWT');
			//     if (value) {
			//         console.log(value);
			// 		global.user_data.jwt = value;
			// 		//global.isLogin = true;
			//     }
			// } catch (e) {
			//     // error
			// }
			// // 尝试直接登录
			// if(global.user_data.jwt == null) {return;}
			// //await this.getAllClass();
			// uni.request({
			// 	url:global.base_url+"auto_login/"+global.user_data.jwt,
			// 	method:'GET',
			// 	success: res => { 
			// 		var statusCode = res.data.StatusCode
			// 		var data = res.data.data
			// 		global.user_data.avatarUrl = data.image
			// 		global.user_data.native = data.native_place
			// 		global.user_data.nickNames = data.nickName
			// 		global.user_data.score = data.score
			// 		global.user_data.wx_number = data.wx_number
			// 		global.user_data.sex = data.sex
			// 		global.user_data.accuracy = Math.round(data.success_times*100/data.task_times)
			// 		global.isLogin = true
			// 		console.log(global.isLogin);
			// 		// 刷新jwt，需要这个功能吗？
			// 		//global.user_data.jwt = data.newJWT 
			// 		//console.log(data.newJWT)
			// 		uni.setStorage({
			// 			key:'JWT',
			// 			data:global.user_data.jwt
			// 		})
			// 	},
			// })
			
			
		}
	}
</script>

<style>
	Page {
		font-size: 14px;
	}
 
	.top {
		width: 100%;
		height: 180px;
		background: #23EBB9;
		padding-top: 15px;
		position: relative;
	}
 
	.center {
		width: 95%;
		height: 150px;
		background: white;
		display: flex;
		flex-direction: column;
		margin: 0 auto;
		border-radius: 5px;
	}
 
	.center_top {
		display: flex;
		flex-direction: row;
		width: 80%;
		height: 80px;
		margin: 0 auto;
		margin-top: 20rpx;
		border-bottom: 1px solid #EEEEEE;
	}
 
	.center_img {
		width: 66px;
		height: 66px;
		border-radius: 50%;
		overflow: hidden;
	}
 
	.center_img image {
		width: 100%;
		height: 100%;
		border-radius: 50%;
	}
 
	.center_img .user_head {
		width: 100%;
		height: 100%;
	}
 
	.center_info {
		display: flex;
		flex-direction: column;
		margin-top: 10rpx;
		margin-left: 30px;
	}
 
	.center_name {
		font-size: 20px;
	}
 
	.center_phone {
		color: #BEBEBE;
	}
 
	.center_down {
		display: flex;
		flex-direction: row;
		width: 80%;
		height: 35px;
		margin: 0 auto;
		margin-top: 20rpx;
	}
 
	.center_rank {
		width: 50%;
		height: 35px;
		display: flex;
		flex-direction: row;
	}
 
	.rank_text {
		height: 35px;
		line-height: 35px;
		margin-left: 10rpx;
		color: #AAAAAA;
	}
 
	.center_rank image {
		width: 35px;
		height: 35px;
	}
 
	.center_score {
		width: 50%;
		height: 35px;
		display: flex;
		flex-direction: row;
	}
 
	.center_score image {
		width: 35px;
		height: 35px;
	}
 
	.gif-wave {
		position: absolute;
		width: 100%;
		bottom: 0;
		left: 0;
		z-index: 99;
		mix-blend-mode: screen;
		height: 100rpx;
	}
</style>
