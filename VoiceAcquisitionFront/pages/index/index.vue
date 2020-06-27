<template>
    <view class="uni-page-body" style="box-sizing: border-box;">

        <scroll-view class="" scroll-y="false" :style="'height:'+scrollHeight+'px;'">

            <view class="list">
                <view class="li">
                    <view class="uni-row uni-flex" style="justify-content: space-between;background: #fff;padding: 10px;">

                        <view class="uni-flex" style="align-self: center;width: 160upx;">
                            标题
                        </view>
                        <input :class="form.title?'':'red'" type="text" v-model="form.title" placeholder="请输入标题" style="background: #f3f3f3;padding: 5px;flex: 1;" />
					</view>
                </view>
				<view class="list uni-row uni-flex" style="background: #FFFFFF;">
				

				    <view class="uni-flex uni-flex-item" style="padding: 5px;">
				        <view class="uni-flex uni-column" style="width: 100%;box-sizing: border-box;background: #f5f5f5;">
				            <textarea v-model="form.text" placeholder="请输入内容" style="padding: 10px;width: 100%;box-sizing: border-box;" />
				            </view>
				    </view>
				</view>
						
				<view  class="li">
					<view class="uni-row uni-flex" style="justify-content: space-between;background: #fff;padding: 10px;">
							<label>金额</label>
							<view style="width: 40%;">
							    <numSelect model="2" color="#6fb1f9" @getValue="getValue" input="true"></numSelect>
							</view>
							<label>阈值</label>
							<view style="width: 40%;">
							    <numSelect model="2" color="#6fb1f9" @getValue="getValue" input="true"></numSelect>
							</view>
					</view>
				</view>
				
				<view  class="li">
					<view class="uni-row uni-flex" style="justify-content: space-between;background: #fff;padding: 24.5px;">
							<button  type="default" style="width: 50%;" @tap="send">提交</button>
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
				localPath: ''
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
			chooseFile:function(){
				uni.chooseImage({
					count: 1,
					success:function(res){
						console(res)
					}
				})
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
