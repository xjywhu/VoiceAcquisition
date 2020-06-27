<template>
</template>

<script>
	export default {
		data() {
			return {
				
			}
		},
		methods: {
			
		},
		onLoad: function(option) {
			uni.getProvider({
				service:'payment',
				success:function(res){
					payment(data).then(res=>{
							let result = res.data.data;
							uni.showLoading({});
							if(res.statusCode == 200){
								uni.hideLoading();
								uni.requestPayment({
									provider:'wxpay',
									appId:result.appId,
									timeStamp:result.timeStamp,
									nonceStr:result.nonceStr,
									package:result.package,
									signType:'MD5',
									paySign:result.paySign,
									success:function(res){
										showTips('支付成功')
										//此处联系服务器更改用户积分值
										
										setTimeout(() => { //支付成功跳转
											callback();
										}, 1200)
									},
									fail: function(err) => {
										showTips('支付失败')
										setTimeout(() => { //支付失败跳转
											callback()
										})
									}
								})
							}
						}
					);
				}
			});
			// uni.requestPayment({
			// 	provider:'wxpay',
			// 	//timeStamp:
			// 	signType:'MD5'
			// });
		}
	}
</script>

<style>
</style>
