<template>
	<div id="number-panels" v-on:click.stop.self="selectNumber(-1)">
		<h2>Choose Number</h2>
		<ul v-on:click.stop.self="selectNumber(-1)">
			<li v-for="i in 9" v-on:click="selectNumber(i)" v-bind:class="{ invisible: board.indexOf(i) >= 0 }">
				<span>{{ i }}</span>
			</li>
			<li v-on:click="selectNumber(0)">
				<span>clear</span>
			</li>
		</ul>
	</div>
</template>

<script>
export default {
  name: "number-panels",
  props: ["board", "selectNumber"],
}
</script>

<style>
#number-panels {
	position: absolute;
	top: 0px;
	left: 0px;
	override: hidden;
	width: 100%;
	height: 100%;
	background-color: rgba(150, 150, 150, 0.8);
	text-align: center;
}
#number-panels ul {
	position: relative;
	width: 100%;
	height: 100%;
	margin: 0 auto;
	max-width: 600px;
}
#number-panels ul li{
	position: relative;
	padding: 10% 10% 10% 10%;
	margin: 1% 1% 0% 0%;
	border: 1px solid;
	width: 30%;
	float: left;
	list-style: none;
	text-align: center;
	vertical-align: middle;
}
#number-panels ul li:last-child {
	width: 92%;
}
#number-panels .invisible {
	visibility: hidden;
}
</style>
