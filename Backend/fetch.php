<?php
require_once('conn.php');
$fetched=array();
$query="select * from violations";
$result=mysqli_query($conn,$query);
if($result)
{
	while($row=mysqli_fetch_array($result,MYSQLI_NUM))
	{
		array_push($fetched,array('violations'=> $row[0],));
	}
}
else{
	echo"error";
}
echo json_encode($fetched);
?>