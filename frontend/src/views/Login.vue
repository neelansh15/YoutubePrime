<template>
	<v-container fill-height>
		<v-row align="center" justify="center">
			<v-card width="500">
				<v-card-title class="text-h4">Login</v-card-title>
				<v-alert type="error" v-if="!validCred">INVALID CRED</v-alert>
				<v-card-text>
					<v-form v-model="valid" @submit.prevent="login">
						<v-row>
							<v-col>
								<v-text-field
									v-model="email"
									:rules="nameRules"
									label="Email"
									outlined
									required
								></v-text-field>
							</v-col>
						</v-row>
						<v-row>
							<v-col>
								<v-text-field
									type="password"
									v-model="password"
									:rules="passwordRules"
									label="Password"
									outlined
									required
								></v-text-field>
							</v-col>
						</v-row>
						<v-btn type="submit" depressed>Log in</v-btn> <br />
						<div class="ml-1 mt-3">
							Don't have an account?
							<v-btn to="/register" text small>Sign up</v-btn>
						</div>
					</v-form>
				</v-card-text>
			</v-card>
		</v-row>
	</v-container>
</template>

<script>
import axios from 'axios'

export default {
	data() {
		return {
			email: '',
			password: '',
			valid: null,
			validCred: true,
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
			// if (!this.valid) return

			const inputEmail = this.email
			const inputPassword = this.password
			console.log(inputEmail, inputPassword)

			axios
				.post('http://127.0.0.1:5000/login', {
					email: inputEmail,
					password: inputPassword,
				})
				.then(res => {
					console.log(res)
					const token = res.data
					console.log(res.status)
					this.$store.commit('setToken', token)
					console.log(token)
					this.$router.push({ name: 'Dashboard' })
				})
				.catch(error => {
					const err = error
					if (err.response) {
						this.validCred = false
						console.log(err.response.status)
						console.log(err.response.data)
					}
				})
		},
	},
}
</script>

<style></style>
