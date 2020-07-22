<template>
       <m-slide-list :data="list" :button="buttonList" :border="true" @click="clickMethod" @change="changeMethod"></m-slide-list>
</template>

<script>
	import mSlideList from '../../components/m-slide-list/m-slide-list.vue'
	export default {
	    components: {
	        mSlideList
	    },
		data() {
			return {
		        list : [],
		                buttonList: [
		                    {
		                        title: '分享',
		                        background: '#c4c7cd'
		                    },
		                    {
		                        title: '删除',
		                        background: '#ff3b32'
		                    }
		                ]
		            };
		},
		methods: {  
			onLoad:function(){
				uni.showLoading({
					title:"加载中...."
				})
				uni.request({
					//url: global.base_url+'task_finish/'+global.user_data.wx_number+'/',
					//global.base_url+'task_finish/oVCRb5GmyJlyChS90erPLg-Jlz6c/',
					url: global.base_url+'task_finish/'+global.user_data.jwt,
					method: 'GET',
					data: {},
					success: res => {
						console.log(res)
						for (var i=0;i < res.data.data.length;i++)
						{
							var dic =  { "id":res.data.data[i].context.cid, "detail":res.data.data[i].context.sentence, 
							"surname":res.data.data[i].quality, "slide_x":1,rightDetail:res.data.data[i].context.finished_times};
							console.log(dic);
							this.list.push(dic);
						}
						uni.hideLoading();
					},
					fail: () => {},
					complete: () => {}
				});
			},
		    changeMethod(data, button, index){
		        console.log('滑动按钮回调', data)
		        console.log('滑动按钮回调', button)
		    },
		    clickMethod(data){
		        console.log('点击行回调', data)
		    }
		}
	}
</script>

<style lang="scss" scoped>
   
</style>
