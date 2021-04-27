$ServerInstance = "sql-spamapp.database.windows.net"
$databasename = "db-spamapp"
$dbpassword = <password here>
$dbusername = 'sqladmin'

#Delete row for sent email

function deleteEmailRow{
param([string]$email, [string]$subject, [string]$text, [string]$date, [string]$time)

Write-Output "Passed parameters $email $subject $text $date $time"

$query = "DELETE FROM Mails WHERE [email]='$email' AND [subject]='$subject' AND [text]='$text' AND [date]='$date' AND [time]='$time'"

Write-Output "Delete Query: $query"

$params = @{
 'Database' = $databasename
 'ServerInstance' = $ServerInstance
 'Username' = $dbusername
 'Password' = $dbpassword
 'Query' = $query
}
Invoke-Sqlcmd @params
}


function sendEmail{
 param([string]$email, [string]$subject, [string]$text)


 # Create a body for sendgrid
$Body = @{
    "personalizations" = @(
        @{
            "to"      = @(
                @{
                    "email" = $email
                    "name"  = "Receiving party"
                    
                }
            )
            "subject" = $subject
        }
    )
    "content"          = @(
        @{
            "type"  = "text/plain"
            "value" = $text
        }
    )
    "from"             = @{
        "email" = "Jankowski_63776@cloud.wsb.wroclaw.pl"
        "name"  = "Sending party"
    }
}

$BodyJson = $Body | ConvertTo-Json -Depth 4

    $Header = @{
        "authorization" = "Bearer <Bearer token here>"
    }
    #send the mail through Sendgrid
    $Parameters = @{
        Method      = "POST"
        Uri         = "https://api.sendgrid.com/v3/mail/send"
        Headers     = $Header
        ContentType = "application/json"
        Body        = $BodyJson
    }
    Invoke-RestMethod @Parameters
}



#Get mail parameters from Azure SQL Database

$params = @{
 'Database' = $databasename
 'ServerInstance' = $ServerInstance
 'Username' = $dbusername
 'Password' = $dbpassword
 'Query' = 'SELECT [email], [subject], [text], [date], [time] FROM Mails WHERE DATEADD(HOUR, +2, GETUTCDATE()) >= CAST (([date] + '' '' + [time]) AS datetime2)'
}
Write-Output "Zaczynamy..."
$result=Invoke-Sqlcmd @params

foreach ($Row in $result)
{ 
  Write-Output "Select: $($Row[0]) $($Row[1]) $($Row[2]) $($Row[3]) $($Row[4])"
  sendEmail -email $($Row[0]) -subject $($Row[1]) -text $($Row[2])
  Write-Output "email sent"
  deleteEmailRow -email $($Row[0]) -subject $($Row[1]) -text $($Row[2]) -date $($Row[3]) -time $($Row[4])
  Write-Output "Row deleted"

}
Write-Output "To juz koniec..."


