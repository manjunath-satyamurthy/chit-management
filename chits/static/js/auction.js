// start_time = $('.auction_time').val().split(':')
// start_hour = start_time[0]
// start_minute = start_time[1]

// start_time_secs = (parseInt(start_hour) * 60 * 60) + (parseInt(start_minute) * 60) 


// 

// remaining_time_secs = start_time_secs - now_time_secs
// remaining_hours = parseInt(remaining_time_secs/3600) % 24;
// remaining_minutes = parseInt(remaining_time_secs/60) % 60;
// remaining_seconds = 59

// setInterval(function(){
// 	if (remaining_seconds > 0){
// 		remaining_seconds = remaining_seconds -1
// 	}

// 	else if (remaining_minutes > 0){
// 		remaining_minutes = remaining_minutes -1
// 		remaining_seconds = 59;
// 	}
// 	else {
// 		remaining_hours = remaining_hours - 1
// 		remaining_seconds = 59;
// 		remaining_minutes = 59;
// 	}
// 	rtime = String(remaining_hours)+':'+String(remaining_minutes)+':'+String(remaining_seconds)
// 	$('.display_remaining_time').empty().append(String(rtime))
// }, 1000);


now = new Date();
now_hour = now.getHours();
now_minutes = now.getMinutes();
now_seconds = now.getSeconds();

now_time_secs = (now_hour * 60 * 60) + (now_minutes * 60) + now_seconds

auctions = $('.auctions');


for (i=0; i<auctions.length; i++){
	auction = auctions[i];
	console.log($(auction).find('input').val());
	start_time = $(auction).find('input').val().split(':');
	start_hour = start_time[0];
	start_minute = start_time[1];
	start_time_secs = (parseInt(start_hour) * 60 * 60) + (parseInt(start_minute) * 60);
	remaining_time_secs = start_time_secs - now_time_secs;
	remaining_hours = parseInt(remaining_time_secs/3600) % 24;
	console.log(remaining_hours)
	remaining_minutes = parseInt(remaining_time_secs/60) % 60;
	remaining_seconds = remaining_time_secs % 60;
	(function (remaining_seconds, remaining_minutes, remaining_hours, auction){
		setInterval(function(){
			if (remaining_seconds > 0){
				remaining_seconds = remaining_seconds -1
			}

			else if (remaining_minutes > 0){
				remaining_minutes = remaining_minutes -1
				remaining_seconds = 59;
			}
			else if (remaining_seconds == 0 && remaining_minutes == 0){
				remaining_hours = remaining_hours - 1
				remaining_seconds = 59;
				remaining_minutes = 59;
			}
			rtime = String(remaining_hours)+':'+String(remaining_minutes)+':'+String(remaining_seconds)
			$(auction).find('div.display_remaining_time').empty().append(String(rtime))
		}, 1000);
	})
	(remaining_seconds, remaining_minutes, remaining_hours, auction);
}
