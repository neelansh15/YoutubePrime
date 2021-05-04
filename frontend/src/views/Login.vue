<template>
	<div>
		<v-card>
			<v-form v-model="valid">
				<v-row>
					<v-col>
						<v-text-field
							v-model="email"
							:rules="nameRules"
							label="Email"
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
				<v-btn to="/register">Sign up</v-btn>
			</v-form>
		</v-card>
	</div>
</template>

<script>
import axios from 'axios'

export default {
	data() {
		return {
			email: '',
			password: '',
			valid: null,
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
			// this should use email and password
			if (!this.valid) return

			this.$store
				.dispatch('userLogin', {
					email: this.email,
					password: this.password,
				})
				.then(() => {
					this.$router.push({ name: 'Dashboard' })
				})
				.catch(err => {
					console.log(err)
				})
			const inputEmail = this.email
			const inputPassword = this.password
			console.log(inputEmail, inputPassword)
			axios
				.post('http://127.0.0.1:5000/login/', {
					email: inputEmail,
					password: inputPassword,
				})
				.then(res => {
					console.log(res)
				})
		},
	},
}
</script>

<style></style>
