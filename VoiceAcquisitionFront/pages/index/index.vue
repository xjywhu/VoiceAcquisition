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
		                list : [
		                    {
		                        id: 1,
		                        image: '',
		                        title: '张三',
		                        rightDetail: '2019-03-18',
		                        detail: 'XXXXXXXXXXXXXXXXXXX公司',
		                        slide_x: 0
		                    },
		                    {
		                        id: 2,
		                        surname: '李',
		                        title: '李二',
		                        rightDetail: '2019-03-17',
		                        detail: 'XXXXXXXXXXXXXXXXXXX公司',
		                        slide_x: 0
		                    },
		                    {
		                        id: 3,
		                        title: '王五',
		                        rightDetail: '2019-03-18',
		                        slide_x: 0
		                    },
		                    {
		                        id: 4,
		                        surname: '李',
		                        detail: 'XXXXXXXXXXXXXXXXXXX公司',
		                        slide_x: 0
		                    }
		                ],
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
							url: global.base_url+'task_finish/oVCRb5GmyJlyChS90erPLg-Jlz6c/',
							method: 'GET',
							data: {},
							success: res => {
								console.log(res.data);
								//console.log(res.data[0].description);
								this.tasks = res.data;
								uni.hideLoading();
							},
							fail: () => {},
							complete: () => { console.log(url);}
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
