Add-Type -AssemblyName System.Speech
$synth = New-Object System.Speech.Synthesis.SpeechSynthesizer

# Select voice (Microsoft Zira Desktop is clear and natural, or David)
try {
    $synth.SelectVoice("Microsoft Zira Desktop")
} catch {
    try {
        $synth.SelectVoice("Microsoft David Desktop")
    } catch {}
}

$synth.Rate = 1  # Natural professional pacing

$audioDir = "D:\paypal-ai-main\paypal-ai-main\submission_assets\temp_audio"
if (-not (Test-Path $audioDir)) {
    New-Item -ItemType Directory -Path $audioDir -Force | Out-Null
}

$scripts = @{
    "s01" = "Every year, cross-border merchants lose billions when network timeouts strike checkout. An HTTP 504 gateway timeout occurs: the customer assumes the payment failed and clicks pay again, causing catastrophic double billing. PayBridge AI resolves this ambiguity with mathematical truth before duplicate charges occur."
    "s02" = "Unlike fragile black-box automation, PayBridge AI is built on strict financial invariants. Our golden rule: AI never moves money. Autonomous agents analyze evidence and produce formal claims, but only authenticated human operators can authorize mutations through protected, single-attempt cryptographic locks."
    "s03" = "Here in the enterprise dashboard, operations teams monitor active payment cases in real time. Notice our three-dimensional state vector: tracking PayPal gateway ground truth, internal application state, and recipient bank settlement simultaneously to expose discrepancies the moment they emerge."
    "s04" = "Let's launch Golden Path Demo B. We initiate a genuine PayPal sandbox order. As capture processes, we simulate a severe upstream network drop. Instead of crashing or letting the buyer blindly retry, PayBridge instantly locks the checkout session with DO NOT REPEAT CHECKOUT."
    "s05" = "Behind the scenes, our multi-agent DAG investigates autonomously. Agent A01 fetches PayPal ground-truth capture telemetry, while Agent A03 verifies signed webhook signatures. Every agent's analytical claim is strictly validated against an immutable SHA-256 evidence vault before entering the state reducer."
    "s06" = "The Truth Gap Graph provides instant visual clarity. Here we see the precise asymmetry: PayPal successfully captured the funds, but the confirmation response was dropped in transit. The engine classifies this as Gap Zero-One: a confirmed capture requiring immediate customer reassurance."
    "s07" = "PayBridge delivers coordinated two-lens transparency. The buyer's portal clearly explains that their payment succeeded and instructs them not to retry. Simultaneously, the merchant portal confirms receipt, keeping both parties in complete lockstep without contradictory customer support tickets."
    "s08" = "When truth is reached, PayBridge issues an immutable Payment Truth Passport. Backed by SHA-256 cryptographic hashes and signed evidence references, this passport serves as undeniable legal and financial proof of payment for merchants, customers, banks, and auditors alike."
    "s09" = "With conversational intelligence powered by our private sub-second SLM, operations teams get instant natural-language truth. PayBridge AI turns chaotic payment timeouts into verified financial certainty. One payment, two parties, one immutable truth. Thank you."
}

foreach ($key in ($scripts.Keys | Sort-Object)) {
    $outPath = Join-Path $audioDir "$key.wav"
    Write-Host "Generating voice narration for $key -> $outPath"
    $synth.SetOutputToWaveFile($outPath)
    $synth.Speak($scripts[$key])
    $synth.SetOutputToNull()
    $size = (Get-Item $outPath).Length
    Write-Host "  Success: $key.wav ($size bytes)"
}

$synth.Dispose()
Write-Host "All voice narration segments generated successfully!"
