<template>
	<view>
		<!-- 基本用法 -->
<!-- 		<uni-search-bar @confirm="search" @input="input" ></uni-search-bar> -->
		<view class="content">
			<view class="uni-list">
				<view class="uni-list-cell" @tap="toSpeech" hover-class="uni-list-cell-hover" v-for="(item,index) in tasks" :key="index" :data-cid="item.cid" :data-sentence="item.sentence" :data-threshold_value="item.threshold_value" :data-base_score="item.base_score">
					<uni-card
						mode="basic" 
						:is-shadow="true" 
						:note="'积分:'+item.base_score"
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
	export default {
		//components: {uni-search-bar},
		components: {uniSearchBar},
		data() {
			return {
				tasks : [],
			};
		},
		onLoad:function(){
			uni.showLoading({
				title:"加载中....",
				mask:true
			})
			uni.request({
				url: global.base_url + 'context_info/'+global.user_data.jwt,
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
				title:"加载中....",
				mask:true
			})
			uni.request({
				url: global.base_url + 'context_info/'+global.user_data.jwt,
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
				var score = e.currentTarget.dataset.base_score;
				//console.log(e.currentTarget.dataset);
				uni.navigateTo({
					url: '/pages/Speech/Speech?cid='+cid+'&sentence='+sentence+'&threshold='+threshold+'&score='+score,
				});
			}
		},
	}
</script>

<style>
</style>
