<template>
    <view class="uni-page-body" style="box-sizing: border-box;">

        <scroll-view class="" scroll-y="false" :style="'height:'+scrollHeight+'px;'">

            <view class="list">
                <view class="li">
                    <view class="uni-row uni-flex" style="justify-content: space-between;background: #fff;padding: 10px;">

                        <view class="uni-flex" style="align-self: center;width: 160upx;">
                            标题
                        </view>
                        <input :class="form.title?'':'red'" type="text" v-model="title" placeholder="请输入标题" style="background: #f3f3f3;padding: 5px;flex: 1;" />
					</view>
                </view>
				<view class="list uni-row uni-flex" style="background: #FFFFFF;">
				

				    <view class="uni-flex uni-flex-item" style="padding: 5px;">
				        <view class="uni-flex uni-column" style="width: 100%;box-sizing: border-box;background: #f5f5f5;">
				            <textarea v-model="description" placeholder="请输入内容" style="padding: 10px;width: 100%;box-sizing: border-box;" />
				            </view>
				    </view>
				</view>
						
				<view  class="li">
					<view class="uni-row uni-flex" style="justify-content: space-between;background: #fff;padding: 10px;">
							<label>金额</label>
							<view style="width: 40%;">
							    <numSelect model="2" color="#6fb1f9" @getValue="getMoney" input="true"></numSelect>
							</view>
							<label>阈值</label>
							<view style="width: 40%;">
							    <numSelect model="2" color="#6fb1f9" @getValue="getThreshold" input="true"></numSelect>
							</view>
					</view>
				</view>
				
				<view  class="li">
					<view class="uni-row uni-flex" style="justify-content: space-between;background: #fff;padding: 24.5px;">
							<button  type="default" style="width: 50%;" @tap="submit">提交</button>
					</view>
				</view>
				
            </view> 
        </scroll-view>
     
    </view>
</template>

<script>
	import numSelect from '../../components/poiuy-numSelect/numSelect.vue'
	import lFile from'../../components/l-file/l-file.vue'
    export default {
		data() {
			return {
				localPath: '',
				title: '',
				money: '',
				threshold: '',
				description:'',
			}
		},
        components: {
			numSelect
        },
        onLoad:function(){
        	// uni.chooseImage({
        	// 	count:1,
        	// 	success:function(res){
        	// 		console.log(res);
        	// 	}
        	// })
        },
		methods:{
			getMoney:function(e){
				this.money = e;
			},
			getThreshold:function(e){
				this.threshold = e;
			},
			submit:function(){
				console.log(this.title);
				console.log(this.description);
				console.log(this.money);
				console.log(this.threshold);
				/*uni.request({
				url: "http://127.0.0.1:8000/api/v1/tasks/", //仅为示例，并非真实接口地址。
				data: {
				phoneNumber: _self.phoneNumber
				},
				method: 'POST',
				header: {
				// 'custom-header': 'hello' //自定义请求头信息
				},
				success: (res) => {
				console.log(res.data);
				/*if(res.data.success){
				_self.$api.msg(res.data.msg);
				}else{
				_self.$api.msg(res.data.msg);
				}*/
				///},
				/*fail: (res) => {
				//_self.$api.msg('发送失败');
				console.log(res)
				}
				});*/

				
				
			},
			
		}
    }
</script>

<style lang="scss" scoped>
    .uni-page-body {
        background: rgb(240, 240, 240);
    }

    .color-nav {
        flex-direction: column;
        box-sizing: border-box;
        width: 0px;
        padding: 5px 12px;
        justify-content: center;
        align-items: center;
    }

    .red {
        border: 1px solid #DD524D;
    }

    .list {
        background: rgb(240, 240, 240);
        padding: 5px 0;
        box-sizing: border-box;

        .li {
            padding: 0.5px 0;
            box-sizing: border-box;
        }
    }
</style>
