<?php
//Contact Page File
if (isset($_POST['email'])) {

// Email info
  $admin_email = "admin@melzy.co.za";
  $name = $_POST['name'];
  $email = $_POST['email'];
  $phone = $_POST['phone'];
  // $subject = $_POST['subject'];
  $message = $_POST['message'];

// To send the email
  mail($admin_email, "General Enquiry", $message . ' - ' . $phone, "From:" . $email);
  header('Location: http://melzy.co.za/student_rentals.html');
}
