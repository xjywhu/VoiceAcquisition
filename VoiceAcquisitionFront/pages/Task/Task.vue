<template>
	<view>
		<!-- 基本用法 -->
		<uni-search-bar @confirm="search" @input="input" ></uni-search-bar>
		<view class="content">
			<view class="uni-list">
				<view class="uni-list-cell" @tap="toSpeech" hover-class="uni-list-cell-hover" v-for="(item,index) in tasks" :key="index" :data-cid="item.cid" :data-sentence="item.sentence" :data-threshold_value="item.threshold_value">
					<uni-card
						mode="basic" 
						:is-shadow="true" 
						note="金额:100"
						:threshold="'阈值:'+item.threshold_value"
					>
					{{item.sentence}}
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
				url: base_url + 'context_info/'+global.user_data.jwt,
				method: 'GET',
				data: {},
				success: res => {
					console.log(res.data.data);
					//console.log(res.data[0].description);
					this.tasks = res.data.data;
					uni.hideLoading();
				}, 
				fail: () => {console.log("fail.........");},
				complete: () => {}
			});
		},
		onShow:function(){
			uni.showLoading({
				title:"加载中...."
			})
			uni.request({
				url: base_url + 'context_info/'+global.user_data.jwt,
				method: 'GET',
				data: {},
				success: res => {
					console.log(res.data.data); 
					//console.log(res.data[0].description);
					this.tasks = res.data.data;
					uni.hideLoading();
				}, 
				fail: () => {console.log("fail.........");},
				complete: () => {}
			});
		},
		methods: { 
			toSpeech(e){
				var cid = e.currentTarget.dataset.cid;
				var sentence = e.currentTarget.dataset.sentence;
				var threshold = e.currentTarget.dataset.threshold_value;
				//console.log(e.currentTarget.dataset);
				uni.navigateTo({
					url: '/pages/Speech/Speech?cid='+cid+'&sentence='+sentence+'&threshold='+threshold,
				});
			}
		},
	}
</script>

<style>
</style>
