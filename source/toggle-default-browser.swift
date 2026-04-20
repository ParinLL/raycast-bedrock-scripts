#!/usr/bin/swift

// This file is invoked by toggle-default-browser.sh.
// Raycast metadata is intentionally kept in the .sh wrapper.

import AppKit

// --- Configuration ---
let browsers: [(name: String, id: String, path: String)] = [
    ("Brave",  "com.brave.Browser", "/Applications/Brave Browser.app"),
    ("Chrome", "com.google.Chrome", "/Applications/Google Chrome.app"),
]

// --- Detect current default browser ---
func getCurrentBundleID() -> String {
    guard let url = URL(string: "https://example.com"),
          let appURL = NSWorkspace.shared.urlForApplication(toOpen: url),
          let bundle = Bundle(url: appURL),
          let bid = bundle.bundleIdentifier else {
        return ""
    }
    return bid
}

// --- Set default browser via NSWorkspace (macOS 12+) ---
func setDefaultBrowser(appPath: String) -> Bool {
    let appURL = URL(fileURLWithPath: appPath)
    let sema = DispatchSemaphore(value: 0)
    var success = false

    // Setting "http" scheme is sufficient — macOS applies it to https as well
    NSWorkspace.shared.setDefaultApplication(at: appURL, toOpenURLsWithScheme: "http") { error in
        success = (error == nil)
        sema.signal()
    }
    sema.wait()
    return success
}

// --- Main ---
let currentID = getCurrentBundleID()
let currentIndex = browsers.firstIndex(where: { $0.id.caseInsensitiveCompare(currentID) == .orderedSame }) ?? 0
let targetIndex = (currentIndex + 1) % browsers.count
let target = browsers[targetIndex]

if setDefaultBrowser(appPath: target.path) {
    print("✅ Default browser → \(target.name)")
} else {
    print("❌ Failed to switch to \(target.name)")
}
