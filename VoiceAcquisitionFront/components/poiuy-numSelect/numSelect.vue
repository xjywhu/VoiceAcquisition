<template>
	<view class="num-view">
		<view class="box style1" v-if="model==='1'">
			<text class="iconfont icon-wuuiconsuoxiao" :class="disable?'disable':closeMinus?'disable':''" :style="{color:color,'font-size':size+'rpx'}"
			 @click="minus"></text>
			<input v-model="num" :style="{'font-size':(size*0.7)+'rpx'}" type="digit" @input="numInput" @blur="blur" :maxlength="maxlength"
			 :disabled="disable?true:!input" class="num" :class="disable?'disable':''" />
			<text class="iconfont icon-wuuiconxiangjifangda" :class="disable?'disable':closeAdd?'disable':''" :style="{color:color,'font-size':size+'rpx'}"
			 @click="add"></text>
		</view>

		<view class="box style2" v-if="model==='2'" :style="{border:'1rpx solid '+(disable?'#cccccc':color)}">
			<text class="iconfont icon-jianshao" :class="disable?'disable-txt':closeMinus?'disable-txt':''" :style="{'background-color':color,'font-size':(size*0.6)+'rpx'}"
			 @click="minus"></text>
			<input v-model="num" :style="{'font-size':(size*0.7)+'rpx'}" type="digit" @input="numInput" @blur="blur" :maxlength="maxlength"
			 :disabled="disable?true:!input" class="num" :class="disable?'disable':''" />
			<text class="iconfont icon-jia" :class="disable?'disable-txt':closeAdd?'disable-txt':''" :style="{'background-color':color,'font-size':(size*0.6)+'rpx'}"
			 @click="add"></text>
		</view>

		<view class="box style3" v-if="model==='3'">
			<text class="iconfont icon-fangkuang-jian" :class="disable?'disable':closeMinus?'disable':''" :style="{'color':color,'font-size':size+'rpx'}"
			 @click="minus"></text>
			<input v-model="num" :style="{'font-size':(size*0.7)+'rpx'}" type="digit" @input="numInput" @blur="blur" :maxlength="maxlength"
			 :disabled="disable?true:!input" class="num" :class="disable?'disable':''" />
			<text class="iconfont icon-fangkuang-jia" :class="disable?'disable':closeAdd?'disable':''" :style="{'color':color,'font-size':size+'rpx'}"
			 @click="add"></text>
		</view>

		<view class="box style4" v-if="model==='4'" :style="{border:'1rpx solid '+(disable?'#cccccc':color)}">
			<text class="iconfont icon-jianshao" :class="disable?'disable':closeMinus?'disable':''" :style="{'color':color,'font-size':(size*0.6)+'rpx','border-right':'1rpx solid '+color}"
			 @click="minus"></text>
			<input v-model="num" :style="{'font-size':(size*0.7)+'rpx'}" type="digit" @input="numInput" @blur="blur" :maxlength="maxlength"
			 :disabled="disable?true:!input" class="num" :class="disable?'disable':''" />
			<text class="iconfont icon-jia" :class="disable?'disable':closeAdd?'disable':''" :style="{'color':color,'font-size':(size*0.6)+'rpx','border-left':'1rpx solid '+color}"
			 @click="add"></text>
		</view>

		<view class="box style3" v-if="model==='5'">
			<text class="iconfont  icon-jianshaoshuzi" :class="disable?'disable':closeMinus?'disable':''" :style="{'color':color,'font-size':size+'rpx'}"
			 @click="minus"></text>
			<input v-model="num" :style="{'font-size':(size*0.7)+'rpx'}" type="digit" @input="numInput" @blur="blur" :maxlength="maxlength"
			 :disabled="disable?true:!input" class="num" :class="disable?'disable':''" />
			<text class="iconfont icon-tianjia" :class="disable?'disable':closeAdd?'disable':''" :style="{'color':color,'font-size':size+'rpx'}"
			 @click="add"></text>
		</view>
	</view>
</template>

<script>
	export default {
		name: 'numSelect',
		props: {
			value: { //传入值
				type: Number
			},
			name: { //name 同原生 用于表单提交
				type: String
			},
			min: { //最小值 不做限制则传入null 默认为0
				type: Number,
				default: 0
			},
			max: { //最大值 不做限制则传入null
				type: Number,
				default: 100
			},
			disable: { //是否禁用
				type: Boolean,
				default: false
			},
			color: { //风格颜色 输入颜色代码即可
				type: String,
				default: '#ea5a59'
			},
			model: { //风格类型 默认为1 一共5种
				type: String,
				default: '1'
			},
			input: { //允许输入
				type: Boolean,
				default: false
			},
			step: { //步长
				type: Number,
				default: 1
			},
			size: { //大小
				type: String,
				default: '40'
			}
		},
		data() {
			return {
				num: 0,
				closeMinus: false,
				closeAdd: false,
				maxlength: null,
				isDigit: false
			}
		},
		created() {
			if (this.value || this.value == 0) {
				this.num = this.value;
			}
			this.decideMinus();
			this.decideAdd();
			let len = null;
			if (this.max == null) {
				len = 100000000
			} else {
				len = (this.max + "").length
			}
			if (typeof this.step !== 'Number' && this.step % 1 !== 0) {
				len += 3;
				this.isDigit = true;
			}
			this.maxlength = len;
		},
		watch: {
			value(n, o) {
				this.num = n;
			}
		},
		methods: {
			minus() {
				if (!this.disable) {
					if (this.min || this.min == 0) {
						if (this.num === this.min) {
							return false;
						}
					}
					let v = this.num -= this.step;
					let d = this.isDigit ? Number((v).toFixed(2)) : v
					this.num = d,
						this.closeAdd = false
					if (this.min || this.min == 0) {
						if (this.num === this.min) {
							this.closeMinus = true
						}
					}
				}
				this.output();
			},
			add() {
				if (!this.disable) {
					if (this.max || this.max == 0) {
						if (this.num === this.max) {
							return false;
						}
					}
					let v = this.num += this.step;
					let d = this.isDigit ? Number(v.toFixed(2)) : v
					this.num = d;
					this.closeMinus = false;
					if (this.max || this.max == 0) {
						if (this.num === this.max) {
							this.closeAdd = true
						}
					}
				}
				this.output();
			},

			decideMinus() {
				if (this.num == this.min) {
					this.closeMinus = true
				} else {
					this.closeMinus = false
				}
			},
			decideAdd() {
				if (this.max || this.max == 0) {
					if (this.num == this.max) {
						this.closeAdd = true
						return
					}
				}
				this.closeAdd = false
			},

			numInput(e) {
				let v = e.detail.value;
				if (typeof v !== 'Number' && v % 1 !== 0) {
					this.isDigit = true;
					this.num = (v == "" ? 0 : Number(Number(v).toFixed(2)));
				} else {
					this.num = Number(v == "" ? 0 : v);
				}
				this.output();
			},

			blur(e) {
				if (e.detail.value == "") {
					this.num = 0
				};
				if (this.max || this.max == 0) {
					if (this.num === this.max) {
						this.closeAdd = true
					}
				}

				if (this.min || this.min == 0) {
					if (this.num === this.min) {
						this.closeMinus = true
					}
				}
			},

			output() {
				this.$emit('getValue', this.num);
			}
		}
	}
</script>

<style scoped>
	@font-face {
		font-family: "iconfont";
		src: url('iconfont.eot?t=1592411404392');
		/* IE9 */
		src: url('iconfont.eot?t=1592411404392#iefix') format('embedded-opentype'),
			/* IE6-IE8 */
			url('data:application/x-font-woff2;charset=utf-8;base64,d09GMgABAAAAAASoAAsAAAAACrwAAARbAAEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHEIGVgCDegqHKIVfATYCJAMkCxQABCAFhG0HgRsbFgnIHpKkywYJKMcBBSAQUDz8/xrtvvl/xlcN92RSLXEIySxRNeGxUQKJQ2YWKWH/L6/6VUka8RAL4QRrAFZ2nd7Xp5GOwZr3AX3bm7bmzBjOR5ihrBqRQv/XT4GyAkq5vx9zdaJtC03f9Lf1oma4ZSLHdY6QxDyRKJWFRKPUzjqcyC5e8Jk0pDd/mEBnm+XQ9T2PNzRlcFQgnoTrApo1uzxCD42p6rkwQ3wDRlM8xtUAvobBx39Yhw0UygTwqNv3jhI2o9+YRJH/xKWkgELnxfwyEo4AmfjQ638PVJ4/gtJtX0e7C0xqFKrRbzR4dMvortHEMen/f+rEIJw4FrxhUhGn/8kDpVDIkkqtISrg+kESX+iah6kwiJIxCBGMwYiCcQsiM+5CJMZERMWmiKjZlOwajm8Ns5wai8YbnHhGW6jakISy1AwQ8edl2UqNTUDu1zObh0+1jJxuGzvbOnqJVw3F5ASHTrS+fhZea6qBEDtm4ZDNO3SAHrOz/LaeNGxw+dCkNGaKpcefLl9gpO4gpqLxEtFYMUXLLLXSsurcoGpEp/4mUzEyeariu/rVH/Nvv5JvGwRc/s3xI4gSPvxQvqeL7xsDmcqmTdK7hgC6rD5D1bzpYj1da9JYDZaCXqAURvJJ3qnCgqiFhFsAcz8bypJbOLA5h+mHuJPswrKoxFA1uDFDhLFY18vEGOtCmXX7ZQmpE5M7gynSzgQHM+3KGhxs1WUft7zE68vKL15uyTBFOZvM7wNbX3YcOTY65HJMHgrrdgdGVBWzEWxxVdgS1bqGuEaYvkLPJwKsEsSg4dzJmpAQ+O8wYHbYhul1lf3TglOY7pc7LR9a5dNjdVp7fCoZzdvp3Rdb+EOY9Z4VBGWqg82/5Wd97sPDjxcTro8WPnKdGHd7tOARHh+vSaQW88Pcbo4F11cLwUJ1fdgIGok0/drCJdPlLg5BrwF2zeInwNY4VUQFBmtufmpSzqymflHreY/SH4r8BULw8HdT01Vp+++GowF+ySE8U6XL/2cGaMUfclQGtv7nWKjA0ebN1M0hAq2zmC/IS6fW8FcMz+qlNS6gs4SmpphDobYBSWMPNhOPQKl3BiqNS9A5bO/lvTkJKiLbgUPuMwjTXkBh0ndIptVgM7EHSotmoDIdFHTuhNsNe/sinN2ZQCIiiTfSMfwme5p2Re3Y+iQ9dkRQVQXGl4LQTOGalaubpTN5FFCckpiir5OSNAxJYBf3sMeR4zDGJbBFajQPS4p+yqpVIX1fNL8Z60LbNQEiRIiEbsihcCrm0dz6kXbr55+ILuYQgpEJt+JfJBAyt4/WWGk1AnvWe6gJL+UziRK6tSQRDQoRYC60h3mJo/IMxfXvZyGqyFxYQvZHsUosFILVz09vdN/rTdCBO7eBEYVoxCALsiIbsiMWJl8lx09hWBhzZgqeVqXLrKdbpuaiUjQjdqXQENyLEhONC7MirI2kljToeiirHVvt7DC/X/N5AA==') format('woff2'),
			url('iconfont.woff?t=1592411404392') format('woff'),
			url('iconfont.ttf?t=1592411404392') format('truetype'),
			/* chrome, firefox, opera, Safari, Android, iOS 4.2+ */
			url('iconfont.svg?t=1592411404392#iconfont') format('svg');
		/* iOS 4.1- */
	}

	.iconfont {
		font-family: "iconfont" !important;
		font-style: normal;
		-webkit-font-smoothing: antialiased;
		-moz-osx-font-smoothing: grayscale;
	}

	.icon-wuuiconsuoxiao:before {
		content: "\e61f";
	}

	.icon-wuuiconxiangjifangda:before {
		content: "\e620";
	}

	.icon-jianshao:before {
		content: "\e644";
	}

	.icon-jianshaoshuzi:before {
		content: "\e639";
	}

	.icon-jia:before {
		content: "\e61b";
	}

	.icon-tianjia:before {
		content: "\e673";
	}

	.icon-fangkuang-jia:before {
		content: "\e70e";
	}

	.icon-fangkuang-jian:before {
		content: "\e70f";
	}


	.num-view {
		width: 100%;
	}

	.box {
		display: flex;
		align-items: center;
		justify-content: space-between;
		box-sizing: border-box;
	}

	.box>text {
		font-size: 40rpx;
		transition: all .4s;
		box-sizing: border-box;
	}

	.num {
		width: 80%;
		height: 100%;
		text-align: center;
		font-size: 28rpx;
	}

	.style1 .disable {
		color: #cccccc !important;
		opacity: .5;
	}

	.style2,
	.style4 {
		border-radius: 10rpx;
	}

	.style2>text {
		font-size: 25rpx;
		padding: 10rpx 15rpx;
		color: white;
		border: none;
		border-radius: 8rpx;
	}

	.style2>text:first-child,
	.style4>text:first-child {
		border-top-right-radius: 0rpx;
		border-bottom-right-radius: 0rpx;
	}

	.style2>text:last-child,
	.style4>text:last-child {
		border-top-left-radius: 0rpx;
		border-bottom-left-radius: 0rpx;
	}


	.style2 .disable-txt {
		color: white !important;
		opacity: .5;
		border: none !important;
	}

	.style2 .disable {
		opacity: .5;
		color: #cccccc;
	}


	.style3>text,
	.style1>text {
		font-size: 50rpx;
	}

	.style3 .disable,
	.style4 .disable {
		color: #cccccc !important;
		opacity: .5;
	}

	.style4>text {
		font-size: 25rpx;
		padding: 10rpx 15rpx;
	}
</style>
