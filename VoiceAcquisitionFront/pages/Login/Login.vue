<template>
	<view class="content">
		<!-- #ifdef MP-WEIXIN -->
		<button type="primary" open-type="getUserInfo" @getuserinfo="getuserinfo" withCredentials="true">微信登录</button>
		<!-- #endif -->
		login...
	</view>
</template>

<script>
	export default{
		data() {
		    return {  
		
		    };  
		},
		onLoad:function(){
			
		},
		methods:{
			getuserinfo:function(res){
				if(!res.detail.iv){
					uni.showToast({
						title:"您取消了授权，登录失败",
						icon:"none"
					});
					return false;
				}
				console.log(res);
				// 如果用户授权
				uni.login({
					provider:'weixin',
					success:function(res2){
						var url = 'http://127.0.0.1:8000/api/v1/openid/'+res2.code;
						//console.log(res2.code);
						console.log(res2);
						if(res2.errMsg == "login:ok"){
							uni.request({
								url: url,
								success:function(res3){
									//res3 里面有openid和session_key
									//console.log(res3)
									// console.log(res3.data)
									var openid = res3.data.openid
									global.user_data.wx_number = openid
									//console.log(global.user_data.wx_number)
									console.log('openid:')
									console.log(openid);
									global.user_data.nickNames = res.detail.userInfo.nickName;
									global.user_data.gender = res.detail.userInfo.gender;
									if(global.user_data.gender == 1){
										global.user_data.sex = '男';
									}else if(global.user_data.gender == 2){
										global.user_data.sex = '女';
									}else{
										global.user_data.sex = '未知';
									}
									global.user_data.native = res.detail.userInfo.province.toString();
									global.user_data.wx_number = openid;
									// uni.setStorageSync('wx_number',openid);
									global.isLogin = true;
									console.log('登录成功，即将跳转界面...')
									global.user_data.avatarUrl = res.detail.userInfo.avatarUrl;
									// 存入数据库
									var base_url = "http://127.0.0.1:8000/api/v1/";
									
									
									
									
									uni.navigateBack();
								}
							});
						}else{
							uni.showToast({
								title:"授权失败，请稍后重试",
								icon:"none"
							});
							return false;
						}
					}
				});
			}
		}
	}
</script>

<style>
</style>
