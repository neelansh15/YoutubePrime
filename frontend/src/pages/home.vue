<template>
	<div>
		<banner />
		<v-btn>
			<router-link to="/login"> Login </router-link>
		</v-btn>

		<div>
			<Button label="Hey there!"></Button>
		</div>
	</div>
</template>

<script>
import banner from '../components/banner.vue'
export default {
	components: {
		banner
	},
}
</script>

<style></style>
