<template>
	<v-container fill-height>
		<v-row align="center" justify="center">
			<v-card width="800">
				<v-card-title class="text-h4">Register</v-card-title>

				<v-alert type="error" v-if="!validCred">{{ this.message }}</v-alert>
				<v-card-text>
					<v-form v-model="valid">
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
									v-model="password"
									:rules="passwordRules"
									label="Password"
									outlined
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
									outlined
									required
								></v-text-field>
							</v-col>
						</v-row>
						<v-row>
							<v-col>
								<v-text-field
									v-model="photoUrl"
									label="Photo url"
									outlined
									required
								></v-text-field>
							</v-col>
						</v-row>
						<v-btn @click="register" depressed>Register</v-btn>
						<v-card-text>
							Already have an account?
							<v-btn text small to="/login">Log in</v-btn>
						</v-card-text>
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
			displayName: '',
			photoUrl: '',
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
		register() {
			// this should use email and password
			// if (!this.valid) return

			const inputEmail = this.email
			const inputPassword = this.password
			const inputDisplayName = this.displayName
			const inputPhotoUrl = this.photoUrl
			console.log(inputEmail, inputPassword)
			this.message = ''
			this.validCred = true
			axios
				.post('http://127.0.0.1:5000/register', {
					email: inputEmail,
					password: inputPassword,
					display_name: inputDisplayName,
					photo_url: inputPhotoUrl,
				})
				.then(res => {
					const token = res.data
					this.$store.commit('setToken', token)
					this.$router.push({ name: 'Dashboard' })
				})
				.catch(error => {
					const err = error
					if (err.response) {
						this.validCred = false
						console.log(err.response.status)
						this.message = err.response.data
					}
				})
		},
	},
}
</script>

<style></style>
