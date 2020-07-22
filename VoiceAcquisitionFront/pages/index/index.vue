<template>
	<view>
       <m-slide-list :data="list" :button="buttonList" :border="true" @click="clickMethod" @change="changeMethod"></m-slide-list>
	</view>
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
		    },
			sliceStr:function (str, len) {
			  var len = len || 8;
			  if (str != null) {
			    if (str.length > len) {
			      return str.substring(0, len) + "...";
			    } else {
			      return str;
			    }
			  }
			  return '';
			},
			
			myReplace:function (content) {
			  content = content.replace(" ", "&nbsp;");
			  if (content.indexOf(" ") != -1) {
			    return myReplace(content);
			  }
			
			  return content;
			}

		}
	}
</script>

<style lang="scss" scoped>
   .userinfo {
     display: flex;
     flex-direction: column;
     align-items: center;
   }
   
   .userinfo-avatar {
     width: 128rpx;
     height: 128rpx;
     margin: 20rpx;
     border-radius: 50%;
   }
   
   .userinfo-nickname {
     color: #aaa;
   }
   
   .usermotto {
     margin-top: 0px;
   }
   
   
   .box {
     overflow: hidden;
   }
</style>
