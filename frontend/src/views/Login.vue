<template>
	<div>
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
							:rules="passwordRules"
							label="Password"
							required
						></v-text-field>
					</v-col>
				</v-row>
				<v-btn @click="login">Log in</v-btn>
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
			nameRules: [
				v => !!v || 'Name is required',
				v => (v && v.length < 50) || 'Name must be less than 50 characters',
			],
			passwordRules: [
				v => !!v || 'Password is required',
				v => (v && v.length < 50) || 'Description must be less than 50 characters',
			],
		}
	},
	methods: {
		login() {
			const username = this.username
			const password = this.password
			console.log(username, password)
			axios
				.post('http://127.0.0.1:8000/auth/login/', {
					username: username,
					password: password,
				})
				.then(res => {
					console.log(res)
				})
			console.log(username, password)
		},
	},
}
</script>

<style></style>
