<?php

use PHPMailer\PHPMailer\PHPMailer;
use PHPMailer\PHPMailer\Exception;

require 'vendor/autoload.php';

try {
    $address = $argv[1];
    $name = $argv[2];
    //$attachmentFilename = "certFiles/";
    //$attachmentFilename .= $argv[3];
    $attachmentFilename = $argv[3];

    $host = 'smtp.gmail.com';
    $username = "REDACTED";
    $password = "REDACTED";
    $port = 465;
    //    echo error_reporting(E_STRICT);

    //    require_once('PHPMailer/class.phpmailer.php');
    $mail = new PHPMailer();
    /* $body = str_replace(
        array(
            '[namehere]',
        ),
        array(
            $name,
        ),
        file_get_contents('php_files/welcome.html')
    ); */
    $body = file_get_contents('php_files/welcome.html');

    $mail->IsSMTP();
    $mail->IsHTML(true);

    $mail->SMTPAuth = true;
    $mail->SMTPSecure = "ssl";
    $mail->Host = $host;
    $mail->Port = $port;
    $mail->Username = $username;
    $mail->Password = $password;
    $mail->SetFrom("putra@mudasg.org", "Putra Zayan | MudaSG");


    $mail->AddReplyTo("sherlita@mudasg.org","Sherlita Almeyra");
    $mail->Subject = "Your Certificate of Appreciation from MudaSG";
    $mail->AltBody = "To view the message, please use an HTML compatible email viewer!";
    $mail->MsgHTML($body);
    $mail->AddAddress($address);
    $mail->AddAttachment($attachmentFilename, 'Certificate.pdf');

    $mail->send();

    echo "Email sent to $address";
} catch (Exception $e) {
    echo "Error {$mail->ErrorInfo}";
}
