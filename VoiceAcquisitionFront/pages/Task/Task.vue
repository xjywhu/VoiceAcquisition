<template>
	
	<view>
	<!-- 基本用法 -->
	<uni-search-bar @confirm="search" @input="input" ></uni-search-bar>
	
	<!-- 自定义Placeholder -->
	<uni-search-bar placeholder="自定placeholder" @confirm="search"></uni-search-bar>
	
	<!-- 设置圆角 -->
	<uni-search-bar :radius="100" @confirm="search"></uni-search-bar>	
<!-- 一般用法 -->
<uni-card title="标题文字" thumbnail="https://img-cdn-qiniu.dcloud.net.cn/new-page/uni.png" extra="额外信息" note="Tips">
    内容主体，可自定义内容及样式
</uni-card>
<!-- 内容通栏 -->
<uni-card is-full="true" title="DCloud" thumbnail="https://img-cdn-qiniu.dcloud.net.cn/new-page/uni.png" extra="2018.12.12" >
    <image src="https://img-cdn-qiniu.dcloud.net.cn/uniapp/images/shuijiao.jpg" style="width: 100%;"></image>
</uni-card>

<!-- 图文卡片模式 -->
<uni-card
    title="标题文字"
    mode="style"
    :is-shadow="true"
    thumbnail="https://img-cdn-qiniu.dcloud.net.cn/uniapp/images/cbd.jpg"
    extra="Dcloud 2019-05-20 12:32:19"
    note="Tips"
>
        那是一个秋意盎然、金风送爽的日子，我和父母一起来到了位于上师大旁的康健园。一踏进公园，一股浓郁的桂香扑鼻而来，泌人心脾,让我心旷神怡，只见一朵朵开得正烈的金色桂花，迎风而立，仿佛在向我招手。我们追着这桂香，走进了清幽的公园。
</uni-card>

<!-- 标题卡片模式 -->
<uni-card 
    title="Dcloud" 
    mode="title" 
    :is-shadow="true" 
    thumbnail="https://img-cdn-qiniu.dcloud.net.cn/uniapp/images/muwu.jpg" 
    extra="技术没有上限" 
    note="Tips"
>
    那是一个秋意盎然、金风送爽的日子,我和父母一起来到了位于上师大旁的康健园.一踏进公园,一股浓郁的桂香扑鼻而来,泌人心脾,让我心旷神怡,只见一朵朵开得正烈的金色桂花,迎风而立,仿佛在向我招手.我们追着这桂香,走进了清幽的公园.
</uni-card>

<!-- 自定义底部按钮 -->
<uni-card title="Dcloud" note="true">
    默认内容
    <template v-slot:footer>
        <view class="footer-box">
            <view>喜欢</view>
            <view>评论</view>
            <view>分享</view>
        </view>
    </template>
</uni-card>
</view>
</template>

<script>
	//import uniCard from '@/components/uni-card/uni-card.vue';
	import uniSearchBar from '@/components/uni-search-bar/uni-search-bar.vue';
	export default {
		//components: {uni-search-bar},
		components: {uniSearchBar},
		data() {
			return {
				
			}
		},
		methods: {
			
		}
	}
</script>

<style>

</style>
