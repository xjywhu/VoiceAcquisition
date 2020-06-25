<script>
	global.isLogin = false
	global.user_data = {
		wx_number: 'unknown',
		nickNames: '匿名用户',
		avatarUrl: 'http://img2.imgtn.bdimg.com/it/u=2091711702,2468700162&fm=11&gp=0.jpg',//默认头像路径
		sex: '',
		age: '',
		gender: 0,
		native: '',
		show: '',
		hidden: ''
	}
	export default {
		onLaunch: function() {
			console.log('App Launch')
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
