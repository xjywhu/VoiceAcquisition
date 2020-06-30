<template>
	
	<view>
		<!-- 基本用法 -->
		<uni-search-bar @confirm="search" @input="input" ></uni-search-bar>
<!-- 		<view class="test">
			<div style="display:flex;">
			<uni-tag text="note"  type="success" :circle="false" size="small"></uni-tag>
			<uni-tag text="note"  type="warning" :circle="false" size="small"></uni-tag>
			</div>
		</view> -->
<!-- 		<uni-tag text="标签"></uni-tag>
		<uni-tag text="标签" type="error" :circle="true"></uni-tag>
		<uni-tag text="标签" @click="bindClick"></uni-tag> -->
		<!-- 标题卡片模式 -->
		<view class="content">
			<view class="uni-list">
				<view class="uni-list-cell" hover-class="uni-list-cell-hover" v-for="(item,index) in tasks" :key="index" :data-newsid="item.tid">
					<uni-card
						:title= "item.title"
						@click="toSpeech"
						mode="title" 
						:is-shadow="true" 
						:thumbnail= "base_url+'images/cccccc'"
						:extra="'发布者:'+item.releaser_wx_number"
						:note="'金额:'+item.money"
						:threshold="'阈值:'+item.threshold_value"
					>
					<!-- :thumbnail= "base_url+'images/'+item.releaser_wx_number" -->
					{{item.description}}
					</uni-card>
				</view>
			</view>
		</view>	
	</view>
</template>

<script>
	//import uniCard from '@/components/uni-card/uni-card.vue';
	import uniSearchBar from '@/components/uni-search-bar/uni-search-bar.vue';
	//import uniTag from "@/components/uni-tag/uni-tag.vue";
	var base_url = "http://127.0.0.1:8000/api/v1/";
	export default {
		//components: {uni-search-bar},
		components: {uniSearchBar},
		data() {
			return {
				tasks : [],
				base_url: "http://127.0.0.1:8000/api/v1/",
			};
		},
		onLoad:function(){
			uni.showLoading({
				title:"加载中...."
			})
			uni.request({
				url: base_url + 'tasks',
				method: 'GET',
				data: {},
				success: res => {
					console.log(res.data);
					//console.log(res.data[0].description);
					this.tasks = res.data;
					uni.hideLoading();
				},
				fail: () => {},
				complete: () => {}
			});
		},
		methods: {
			// openinfo(e) {
			// 	var newsid = e.currentTarget.dataset.newsid;
			// 	uni.navigateTo({
			// 		url: '../info/info?newsid='+newsid
			// 	});
			// }
			toSpeech(){
				uni.navigateTo({
					url: '/pages/Speech/Speech',
				});
			}
		},
	}
</script>

<style>
</style>
