use webscrapy

db.createCollection("collectInfo")

db.createUser(
	{
		user: "webscrapy", 
		pwd: "WebScrapy123", 
		roles : [ 
			{ 
				role: "readWrite", 
				db: "webscrapy" 
			} 
		] 
	}
)
