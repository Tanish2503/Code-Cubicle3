-- AppleScript to select text on the screen
tell application "System Events"
    tell process "WhatsApp"
        set frontmost to true
        delay 1
        -- Adjust these coordinates to your specific needs
        click at {450, 60}
        delay 0.2
        keystroke "a" using command down -- Select all text
        delay 0.2
        keystroke "c" using command down -- Copy selected text
    end tell
end tell
