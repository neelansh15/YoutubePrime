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
export default {}
</script>

<style></style>
