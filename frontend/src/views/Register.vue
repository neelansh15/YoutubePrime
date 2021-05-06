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
				<v-row>
					<v-col>
						<v-text-field
							v-model="displayName"
							:rules="nameRules"
							label="Write the name you want to be displayed on your page"
							required
						></v-text-field>
					</v-col>
				</v-row>
				<v-row>
					<v-col>
						<v-text-field
							v-model="photoUrl"
							label="Photo url"
							required
						></v-text-field>
					</v-col>
				</v-row>
				<v-btn to="/login">Log in</v-btn>
				<v-btn @click="register">Sign up</v-btn>
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
			displayName: '',
			photoUrl: '',
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
		register() {
			// this should use email and password
			// if (!this.valid) return

			const inputEmail = this.email
			const inputPassword = this.password
			const inputDisplayName = this.displayName
			const inputPhotoUrl = this.photoUrl
			console.log(inputEmail, inputPassword)

			axios
				.post('http://127.0.0.1:5000/register', {
					email: inputEmail,
					password: inputPassword,
					display_name: inputDisplayName,
					photo_url: inputPhotoUrl,
				})
				.then(res => {
					const token = res.data
					console.log(token)
				})
		},
	},
}
</script>

<style></style>
