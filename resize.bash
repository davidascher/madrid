mdfind -0 -onlyin . "kMDItemPixelHeight > 1440 || kMDItemPixelWidth > 1440" | xargs -0 sips -Z 1440


