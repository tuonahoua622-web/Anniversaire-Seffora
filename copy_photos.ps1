$src = 'C:\Users\DELL\AppData\Local\hermes\cache\images\'
$dst = 'C:\Users\DELL\OneDrive\Desktop\Anniversaire\photos\'
$files = @('img_c4149c8fb5ae.jpg','img_1b4972650cdb.jpg','img_e0652fd0fc3e.jpg','img_883934a03a69.jpg','img_57d58d9df819.jpg','img_714dd30b14ac.jpg')
$i = 1
foreach ($f in $files) {
  Copy-Item (Join-Path $src $f) (Join-Path $dst ("photo" + $i + ".jpg"))
  $i++
}
Get-ChildItem $dst | Select-Object Name, Length
