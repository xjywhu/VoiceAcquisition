<template>
	<view class="content">
		<image class="bg-set" src="https://yanxuan.nosdn.127.net/6b2b28090942b8bdf4c16d63e9226c32.png"></image>
		<view class='takePlaceView'></view>
		<!-- #ifdef MP-WEIXIN -->
		<button type="primary" class='loginBtn' open-type="getUserInfo" @getuserinfo="getuserinfo" withCredentials="true">微信登录</button>
		<!-- #endif -->
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
						var url = global.base_url+'openid/'+res2.code;
						//console.log(res2.code);
						console.log(res2);
						if(res2.errMsg == "login:ok"){
							uni.request({
								url: url,
								success:function(res3){
									//res3 里面有openid和session_key
									//console.log(res3)
									console.log('res3.data:')
									console.log(res3.data)
									var statusCode = res3.data.StatusCode
									if(statusCode == 'fail'){ // 登录失败
										uni.showToast({
										    title: '登录失败，请稍后重试',
										    icon:"none"
										});
										uni.navigateBack();
									}
									var openid = res3.data.data.openid
									var jwt = res3.data.data.jwt
									
									
									global.user_data.jwt = jwt
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
									
									console.log(res)
									
									global.user_data.wx_number = openid;
									// uni.setStorageSync('wx_number',openid);
									global.isLogin = true;
									console.log('登录成功，即将跳转界面...')
									global.user_data.avatarUrl = res.detail.userInfo.avatarUrl;
									// 存入数据库
									if(global.user_data.wx_number!= null){
										var data = {
											wx_number:global.user_data.wx_number,
											nickName : global.user_data.nickNames,
											native_place:global.user_data.native,
											sex:global.user_data.sex,
											age:global.user_data.age,
											image:global.user_data.avatarUrl,
										}
										uni.request({
											url:global.base_url+'user_info/'+jwt,
											data:data,
											method:'PUT',
											success: res => {
												console.log(res.data);
												console.log(res.data.data.score)
												if(res.data.data.success_times==0) global.user_data.accuracy=0;
												else global.user_data.accuracy = Math.round(res.data.data.success_times*100/res.data.data.task_times);
												global.user_data.score = res.data.data.score
											},
											fail: () => {},
											complete: () => {}
										})
									}
									uni.setStorage({
										key:'JWT',
										data:jwt
									})
									setTimeout(()=>{
									uni.navigateBack();
									},2000)
								}
							});
						}else{
							uni.showToast({
								title:"授权失败，请稍后重试",
								icon:"none"
							});
							uni.navigateBack();
						}
					}
				});
			}
		}
	}
</script>

<style>
	.takePlaceView{
		/* height: 50%; */
	}
	.content{
		/* display: flex; */
	}
	.loginBtn{
		position: fixed;
		width: 50%;
		top: 40%;
		left: 25%;
	}
	.bg-set{
	    position: fixed;
	    width: 100%;
	    height: 100%;
	    top: 0;
	    left: 0;
	    z-index: -1;
	}
</style>
