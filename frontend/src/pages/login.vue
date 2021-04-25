<template>
	<div>
		<h1>HEllo</h1>
		<v-card>
			<v-form v-model="valid">
				<v-row>
					<v-col>
						<v-text-field
							v-model="username"
							:rules="nameRules"
							label="Username"
							required
						></v-text-field>
					</v-col>
				</v-row>
				<v-row>
					<v-col>
						<v-text-field
							v-model="password"
							:rules="password"
							label="Password"
							required
						></v-text-field>
					</v-col>
				</v-row>
			</v-form>
		</v-card>
	</div>
</template>

<script>
import axios from 'axios'
export default {
	data() {
		return {
			username: '',
			password: '',
		}
	},
	methods: {
		login() {
			const username = this.username
			const password = this.password
		},
	},
}
</script>

<style></style>
