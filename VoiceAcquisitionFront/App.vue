<script>
	global.isLogin = false
	global.user_data = {
		wx_number: null,
		nickNames: '匿名用户',
		avatarUrl: 'http://img2.imgtn.bdimg.com/it/u=2091711702,2468700162&fm=11&gp=0.jpg',//默认头像路径
		sex: '未知',
		age: '',
		score:0,
		gender: 0,
		native: '',
		show: '',
		hidden: '',
		jwt:null,
	}
	global.base_url = 'http://127.0.0.1:8000/api/v1/'
	export default {
		onLaunch: function() {
			if ($api.getStorage('myJWT'))  { // 如果有值
				uni.getStorage({
					key:'myJWT',
					success: (res) => {
						global.user_data.jwt = res.data
					}
				})
			}
			// 尝试直接登录
			if(global.user_data.jwt == null) return;
			var base_url = "http://127.0.0.1:8000/api/v1/auto_login/";
			uni.request({
				url:base_url+global.user_data.jwt,
				method:'GET',
				success: res => {
					var statusCode = res.data.StatusCode
					var data = res.data.data
					global.user_data.avatarUrl = data.image
					global.user_data.native = data.native_place
					global.user_data.nickNames = data.nickName
					global.user_data.score = data.score
					global.user_data.wx_number = data.wx_number
					global.user_data.sex = data.sex
					global.isLogin = true
					// 刷新jwt，需要这个功能吗？
					global.user_data.jwt = data.newJWT
					uni.setStorage({
						key:'JWT',
						data:global.user_data.jwt
					})
				},
			})
		},
		onShow: function() {
			console.log('App Show')
		},
		onHide: function() {
			console.log('App Hide')
		}
	}
</script>

<style>
	/*每个页面公共css */
</style>
