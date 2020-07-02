<template>
	<view class="root">
		<l-file 
		    ref="lFile" 
		    @up-success="upSuccess"
		></l-file>
	</view>
</template>

<script>
	import lFile from "../../components/l-file/l-file.vue"
	export default{
		components:{
			lFile
		},
		data(){
			return{
				
			};
		}
		
		
	}
</script>

<style>
</style>
