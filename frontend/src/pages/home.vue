<template>
	<div>
		<banner />
		<v-btn>
			<router-link to="/login"> Login </router-link>
		</v-btn>
	</div>
</template>

<script>
import banner from '../components/banner.vue'
export default {
	components: {
		banner,
	},
}
</script>

<style></style>
