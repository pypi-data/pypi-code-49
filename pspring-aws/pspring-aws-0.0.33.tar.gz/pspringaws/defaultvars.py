import pspring

pspring.Configuration.defaults({
	"pspringaws.dynamodb.ttlColumnName":"ttl",
    "pspringaws.dynamodb.ttl":"3600"
})
