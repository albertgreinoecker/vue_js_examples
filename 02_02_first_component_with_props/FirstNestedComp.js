export default {
	props:
		{
			msg1: String,
			msg2: String,
			cnt: Number
		},
      template:
          '<h2> Message1: {{msg1}} <br/>Message2: {{msg2}}<br/> Count: {{cnt}}</h2>'
}