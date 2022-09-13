export default {
	emits: ['anyEvent'],
	methods:
	{
		myClick()
		{
			console.log('Called within nested component');
			this.$emit("anyEvent", "called from myClick");
		}

	},
      template:
		  `<button  @click="$emit('anyEvent')">call parent event directly</button> <br/>
	 		<button  @click="myClick()">call method within nested component</button>`

}