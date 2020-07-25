<script>
	global.isLogin = false
	global.user_data = {
		wx_number: null,
		nickNames: '匿名用户',
		avatarUrl: 'http://img2.imgtn.bdimg.com/it/u=2091711702,2468700162&fm=11&gp=0.jpg',//默认头像路径
		sex: '未知',
		age: '',
		accuracy:0,
		score:0,
		gender: 0,
		native: '',
		show: '',
		hidden: '',
		jwt:null,
	}
	//global.base_url = 'http://127.0.0.1:8000/api/v1/'
	global.base_url = 'http://175.24.105.148:8000/api/v1/'
	export default {
		onLaunch: function() {
			console.log('App Launch')
			// if ($api.getStorage('JWT'))  { // 如果有值
			// 	uni.getStorage({
			// 		key:'JWT',
			// 		success: (res) => {
			// 			global.user_data.jwt = res.data
			// 			console.log("hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh")
			// 			//console.log(global.user_data.jwt)
			// 		}
			// 	})
			// }
			try {
			    const value = uni.getStorageSync('JWT');
			    if (value) {
			        console.log(value);
					global.user_data.jwt = value;
			    }
			} catch (e) {
			    // error
			}
			// 尝试直接登录
			if(global.user_data.jwt == null) return;
			uni.request({
				url:global.base_url+"auto_login/"+global.user_data.jwt,
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
					global.user_data.accuracy = Math.round(data.success_times*100/data.task_times)
					global.isLogin = true
					// 刷新jwt，需要这个功能吗？
					//global.user_data.jwt = data.newJWT 
					//console.log(data.newJWT)
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
