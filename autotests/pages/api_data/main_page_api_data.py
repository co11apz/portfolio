import json


def open_page_api():
    url = "https://www.youtube.com/youtubei/v1/guide?key=AIzaSyAO_FJ2SlqU8Q4STEHLGCilw_Y9_11qcW8&prettyPrint=false"

    payload = json.dumps({
        "context": {
            "client": {
                "hl": "ru",
                "gl": "US",
                "remoteHost": "207.244.71.81",
                "deviceMake": "",
                "deviceModel": "",
                "visitorData": "CgsxdVFBcm8zNDE0ZyiOiqGsBjIKCgJERRIEEgAgOg%3D%3D",
                "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36,gzip(gfe)",
                "clientName": "WEB",
                "clientVersion": "2.20231219.04.00",
                "osName": "Windows",
                "osVersion": "10.0",
                "originalUrl": "https://www.youtube.com/",
                "screenPixelDensity": 1,
                "platform": "DESKTOP",
                "clientFormFactor": "UNKNOWN_FORM_FACTOR",
                "configInfo": {
                    "appInstallData": "CI6KoawGEKihsAUQ2cmvBRDuoq8FEP2fsAUQx4OwBRDnhv8SEJrwrwUQpqCwBRC8-a8FEJqksAUQnouwBRDcgrAFEOmMsAUQ6sOvBRDi1K4FEKKSsAUQuIuuBRDamLAFENWIsAUQlPr-EhDUoa8FEKSgsAUQmPz-EhDh8q8FEKaBsAUQrtT-EhDd6P4SEKn3rwUQl4OwBRDks_4SEPyFsAUQ0-GvBRCJ6K4FEPmfsAUQiOOvBRD6krAFEMyu_hIQj6KwBRCZkbAFENfprwUQqaCwBRCrgrAFEOvo_hIQvYqwBRDSlbAFEM2VsAUQt-r-EhC3768FENCNsAUQvbauBRC9mbAFEOuTrgUQ9fmvBRDJ968FEPufsAUQiIewBRComrAFEKKBsAUQrLevBRC3nbAFEMzfrgUQmZSwBRDnuq8FEL75rwUQ26-vBRClwv4SEKaasAUQ16SwBRDmnrAFELClsAUQ5qOwBQ%3D%3D"
                },
                "screenDensityFloat": 1.25,
                "userInterfaceTheme": "USER_INTERFACE_THEME_DARK",
                "timeZone": "Europe/Moscow",
                "browserName": "Chrome",
                "browserVersion": "120.0.0.0",
                "acceptHeader": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                "deviceExperimentId": "ChxOek14TmpFM016VXlNakk0T1RjeE1EQTNOUT09EI6KoawGGI6KoawG",
                "screenWidthPoints": 1536,
                "screenHeightPoints": 150,
                "utcOffsetMinutes": 180,
                "memoryTotalKbytes": "8000000",
                "mainAppWebInfo": {
                    "graftUrl": "https://www.youtube.com/",
                    "pwaInstallabilityStatus": "PWA_INSTALLABILITY_STATUS_UNKNOWN",
                    "webDisplayMode": "WEB_DISPLAY_MODE_BROWSER",
                    "isWebNativeShareAvailable": True
                }
            },
            "user": {
                "lockedSafetyMode": False
            },
            "request": {
                "useSsl": True,
                "internalExperimentFlags": [],
                "consistencyTokenJars": []
            },
            "adSignalsInfo": {
                "params": [
                    {
                        "key": "dt",
                        "value": "1703429392334"
                    },
                    {
                        "key": "flash",
                        "value": "0"
                    },
                    {
                        "key": "frm",
                        "value": "0"
                    },
                    {
                        "key": "u_tz",
                        "value": "180"
                    },
                    {
                        "key": "u_his",
                        "value": "50"
                    },
                    {
                        "key": "u_h",
                        "value": "864"
                    },
                    {
                        "key": "u_w",
                        "value": "1536"
                    },
                    {
                        "key": "u_ah",
                        "value": "824"
                    },
                    {
                        "key": "u_aw",
                        "value": "1536"
                    },
                    {
                        "key": "u_cd",
                        "value": "24"
                    },
                    {
                        "key": "bc",
                        "value": "31"
                    },
                    {
                        "key": "bih",
                        "value": "150"
                    },
                    {
                        "key": "biw",
                        "value": "1520"
                    },
                    {
                        "key": "brdim",
                        "value": "0,0,0,0,1536,0,1536,824,1536,150"
                    },
                    {
                        "key": "vis",
                        "value": "1"
                    },
                    {
                        "key": "wgl",
                        "value": "true"
                    },
                    {
                        "key": "ca_type",
                        "value": "image"
                    }
                ]
            }
        },
        "fetchLiveState": True
    })
    headers = {
        'authority': 'www.youtube.com',
        'accept': '*/*',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/json',
        'cookie': 'CONSENT=PENDING+917; SOCS=CAISEwgDEgk1ODE3OTQxMTEaAnJ1IAEaBgiAlNCqBg; wide=1; _gcl_au=1.1.1236695019.1702128731; _ga=GA1.1.46170218.1702128973; PREF=f4=4000000&f6=40000000&tz=Europe.Moscow&f7=100&f5=30000&guide_collapsed=true; _ga_VCGEPY40VB=GS1.1.1702217844.6.0.1702217844.0.0.0; VISITOR_PRIVACY_METADATA=CgJERRIEEgAgOg%3D%3D; VISITOR_INFO1_LIVE=1uQAro3414g; YSC=mbg-Ztr7WdQ; GPS=1',
        'origin': 'https://www.youtube.com',
        'referer': 'https://www.youtube.com/',
        'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
        'sec-ch-ua-arch': '"x86"',
        'sec-ch-ua-bitness': '"64"',
        'sec-ch-ua-full-version': '"120.0.6099.129"',
        'sec-ch-ua-full-version-list': '"Not_A Brand";v="8.0.0.0", "Chromium";v="120.0.6099.129", "Google Chrome";v="120.0.6099.129"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-model': '""',
        'sec-ch-ua-platform': '"Windows"',
        'sec-ch-ua-platform-version': '"10.0.0"',
        'sec-ch-ua-wow64': '?0',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'same-origin',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'x-client-data': 'CKm1yQEIj7bJAQimtskBCKmdygEIhZbLAQiWocsBCJv+zAEI+ZjNAQiFoM0BCNy9zQEIj+HNAQiu6c0BCN7szQEIoe7NAQjJ7s0BCIPwzQEIhfDNARin6s0B',
        'x-goog-visitor-id': 'CgsxdVFBcm8zNDE0ZyiOiqGsBjIKCgJERRIEEgAgOg%3D%3D',
        'x-youtube-bootstrap-logged-in': 'false',
        'x-youtube-client-name': '1',
        'x-youtube-client-version': '2.20231219.04.00'
    }
    return url, payload, headers
#
#
#
#
#


def check_header_logo_button_api():
    url = "https://www.youtube.com/youtubei/v1/browse?key=AIzaSyAO_FJ2SlqU8Q4STEHLGCilw_Y9_11qcW8&prettyPrint=false"

    payload = json.dumps({
        "context": {
            "client": {
                "hl": "ru",
                "gl": "GB",
                "remoteHost": "23.106.56.21",
                "deviceMake": "",
                "deviceModel": "",
                "visitorData": "CgsxdVFBcm8zNDE0ZyiO9aCsBjIKCgJERRIEEgAgOg%3D%3D",
                "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36,gzip(gfe)",
                "clientName": "WEB",
                "clientVersion": "2.20231219.04.00",
                "osName": "Windows",
                "osVersion": "10.0",
                "originalUrl": "https://www.youtube.com/",
                "screenPixelDensity": 1,
                "platform": "DESKTOP",
                "clientFormFactor": "UNKNOWN_FORM_FACTOR",
                "configInfo": {
                    "appInstallData": "CI71oKwGEOrDrwUQnouwBRCZkbAFENyCsAUQyfevBRD8hbAFEOeG_xIQ2piwBRDuoq8FENfprwUQvPmvBRCPorAFEPufsAUQieiuBRDd6P4SEKXC_hIQ-Z-wBRCrgrAFEJqksAUQ6-j-EhDSlbAFEKy3rwUQ57qvBRCmoLAFENShrwUQ5LP-EhCigbAFEKn3rwUQx4OwBRCa8K8FELfvrwUQ_Z-wBRDbr68FEKaasAUQt52wBRDMrv4SEKihsAUQ6YywBRC9mbAFEKSgsAUQuIuuBRDM364FEKiasAUQmPz-EhD1-a8FEJT6_hIQiIewBRD6krAFEOHyrwUQvvmvBRC9tq4FENPhrwUQ1YiwBRCikrAFEOuTrgUQ0I2wBRCI468FEOLUrgUQt-r-EhCpoLAFEL2KsAUQpoGwBRDNlbAFENnJrwUQmZSwBRCu1P4SEJeDsAUQ16SwBRCwpbAFEOaesAUQ5qOwBQ%3D%3D"
                },
                "screenDensityFloat": 1.25,
                "userInterfaceTheme": "USER_INTERFACE_THEME_DARK",
                "timeZone": "Europe/Moscow",
                "browserName": "Chrome",
                "browserVersion": "120.0.0.0",
                "acceptHeader": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                "deviceExperimentId": "ChxOek14TmpFMk1UazNOekl4TlRnMk5ERTRNdz09EI71oKwGGI71oKwG",
                "screenWidthPoints": 1536,
                "screenHeightPoints": 150,
                "utcOffsetMinutes": 180,
                "memoryTotalKbytes": "8000000",
                "mainAppWebInfo": {
                    "graftUrl": "/",
                    "pwaInstallabilityStatus": "PWA_INSTALLABILITY_STATUS_CAN_BE_INSTALLED",
                    "webDisplayMode": "WEB_DISPLAY_MODE_BROWSER",
                    "isWebNativeShareAvailable": True
                }
            },
            "user": {
                "lockedSafetyMode": False
            },
            "request": {
                "useSsl": True,
                "internalExperimentFlags": [],
                "consistencyTokenJars": []
            },
            "clickTracking": {
                "clickTrackingParams": "CA8QsV4iEwin1JP8nqiDAxW07E8IHRIqDBg="
            },
            "adSignalsInfo": {
                "params": [
                    {
                        "key": "dt",
                        "value": "1703426703681"
                    },
                    {
                        "key": "flash",
                        "value": "0"
                    },
                    {
                        "key": "frm",
                        "value": "0"
                    },
                    {
                        "key": "u_tz",
                        "value": "180"
                    },
                    {
                        "key": "u_his",
                        "value": "49"
                    },
                    {
                        "key": "u_h",
                        "value": "864"
                    },
                    {
                        "key": "u_w",
                        "value": "1536"
                    },
                    {
                        "key": "u_ah",
                        "value": "824"
                    },
                    {
                        "key": "u_aw",
                        "value": "1536"
                    },
                    {
                        "key": "u_cd",
                        "value": "24"
                    },
                    {
                        "key": "bc",
                        "value": "31"
                    },
                    {
                        "key": "bih",
                        "value": "150"
                    },
                    {
                        "key": "biw",
                        "value": "1520"
                    },
                    {
                        "key": "brdim",
                        "value": "0,0,0,0,1536,0,1536,824,1536,150"
                    },
                    {
                        "key": "vis",
                        "value": "1"
                    },
                    {
                        "key": "wgl",
                        "value": "true"
                    },
                    {
                        "key": "ca_type",
                        "value": "image"
                    }
                ]
            }
        },
        "browseId": "FEwhat_to_watch",
        "inlineSettingStatus": "INLINE_SETTING_STATUS_ON"
    })
    headers = {
        'authority': 'www.youtube.com',
        'accept': '*/*',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/json',
        'cookie': 'CONSENT=PENDING+917; SOCS=CAISEwgDEgk1ODE3OTQxMTEaAnJ1IAEaBgiAlNCqBg; wide=1; _gcl_au=1.1.1236695019.1702128731; _ga=GA1.1.46170218.1702128973; PREF=f4=4000000&f6=40000000&tz=Europe.Moscow&f7=100&f5=30000&guide_collapsed=true; _ga_VCGEPY40VB=GS1.1.1702217844.6.0.1702217844.0.0.0; VISITOR_PRIVACY_METADATA=CgJERRIEEgAgOg%3D%3D; VISITOR_INFO1_LIVE=1uQAro3414g; YSC=mbg-Ztr7WdQ; GPS=1; ST-1b=disableCache=true&itct=CA8QsV4iEwin1JP8nqiDAxW07E8IHRIqDBg%3D&csn=MC45NTU2NzA2NTMyNTU0MTY3&endpoint=%7B%22clickTrackingParams%22%3A%22CA8QsV4iEwin1JP8nqiDAxW07E8IHRIqDBg%3D%22%2C%22commandMetadata%22%3A%7B%22webCommandMetadata%22%3A%7B%22url%22%3A%22%2F%22%2C%22webPageType%22%3A%22WEB_PAGE_TYPE_BROWSE%22%2C%22rootVe%22%3A3854%2C%22apiUrl%22%3A%22%2Fyoutubei%2Fv1%2Fbrowse%22%7D%7D%2C%22browseEndpoint%22%3A%7B%22browseId%22%3A%22FEwhat_to_watch%22%7D%7D',
        'origin': 'https://www.youtube.com',
        'referer': 'https://www.youtube.com/',
        'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
        'sec-ch-ua-arch': '"x86"',
        'sec-ch-ua-bitness': '"64"',
        'sec-ch-ua-full-version': '"120.0.6099.129"',
        'sec-ch-ua-full-version-list': '"Not_A Brand";v="8.0.0.0", "Chromium";v="120.0.6099.129", "Google Chrome";v="120.0.6099.129"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-model': '""',
        'sec-ch-ua-platform': '"Windows"',
        'sec-ch-ua-platform-version': '"10.0.0"',
        'sec-ch-ua-wow64': '?0',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'same-origin',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'x-client-data': 'CKm1yQEIj7bJAQimtskBCKmdygEIhZbLAQiWocsBCJv+zAEI+ZjNAQiFoM0BCNy9zQEIj+HNAQiu6c0BCN7szQEIoe7NAQjJ7s0BCIPwzQEIhfDNARin6s0B',
        'x-goog-visitor-id': 'CgsxdVFBcm8zNDE0ZyiO9aCsBjIKCgJERRIEEgAgOg%3D%3D',
        'x-youtube-bootstrap-logged-in': 'false',
        'x-youtube-client-name': '1',
        'x-youtube-client-version': '2.20231219.04.00'
    }
    return url, payload, headers
#
#
#
#
#


def check_left_menu_main_button_api():
    url = "https://www.youtube.com/youtubei/v1/browse?key=AIzaSyAO_FJ2SlqU8Q4STEHLGCilw_Y9_11qcW8&prettyPrint=false"

    payload = json.dumps({
        "context": {
            "client": {
                "hl": "ru",
                "gl": "US",
                "remoteHost": "207.244.71.81",
                "deviceMake": "",
                "deviceModel": "",
                "visitorData": "CgsxdVFBcm8zNDE0ZyiUraGsBjIKCgJERRIEEgAgOg%3D%3D",
                "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36,gzip(gfe)",
                "clientName": "WEB",
                "clientVersion": "2.20231219.04.00",
                "osName": "Windows",
                "osVersion": "10.0",
                "originalUrl": "https://www.youtube.com/",
                "screenPixelDensity": 1,
                "platform": "DESKTOP",
                "clientFormFactor": "UNKNOWN_FORM_FACTOR",
                "configInfo": {
                    "appInstallData": "CJStoawGEKn3rwUQ_Z-wBRCmgbAFEOrDrwUQzN-uBRD5n7AFEJj8_hIQnouwBRDh8q8FEMyu_hIQ1KGvBRDSlbAFENyCsAUQ4tSuBRC9irAFEKy3rwUQ5LP-EhC8-a8FEJT6_hIQzZWwBRC9mbAFEIiHsAUQj6KwBRD1-a8FENfprwUQpcL-EhDZya8FEKuCsAUQvbauBRD7n7AFENPhrwUQieiuBRDQjbAFENuvrwUQrtT-EhCI468FEKiasAUQuIuuBRCpoLAFELfvrwUQmZGwBRCigbAFEJqksAUQ2piwBRDrk64FEN3o_hIQ6YywBRDHg7AFEL75rwUQ_IWwBRC3nbAFEOe6rwUQopKwBRCZlLAFEJeDsAUQt-r-EhDuoq8FEKSgsAUQyfevBRCmmrAFEKagsAUQmvCvBRDr6P4SEKihsAUQ54b_EhD6krAFENWIsAUQ16SwBRCwpbAFEOajsAUQ5p6wBQ%3D%3D"
                },
                "screenDensityFloat": 1.25,
                "userInterfaceTheme": "USER_INTERFACE_THEME_DARK",
                "timeZone": "Europe/Moscow",
                "browserName": "Chrome",
                "browserVersion": "120.0.0.0",
                "acceptHeader": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                "deviceExperimentId": "ChxOek14TmpFNU1qYzRPRFkwTkRrd05UQXhNZz09EJStoawGGJStoawG",
                "screenWidthPoints": 1536,
                "screenHeightPoints": 306,
                "utcOffsetMinutes": 180,
                "memoryTotalKbytes": "8000000",
                "mainAppWebInfo": {
                    "graftUrl": "/",
                    "pwaInstallabilityStatus": "PWA_INSTALLABILITY_STATUS_CAN_BE_INSTALLED",
                    "webDisplayMode": "WEB_DISPLAY_MODE_BROWSER",
                    "isWebNativeShareAvailable": True
                }
            },
            "user": {
                "lockedSafetyMode": False
            },
            "request": {
                "useSsl": True,
                "internalExperimentFlags": [],
                "consistencyTokenJars": []
            },
            "clickTracking": {
                "clickTrackingParams": "CB8Q8KgHGAAiEwijnIXbuaiDAxXRB9YAHdqdBAI="
            },
            "adSignalsInfo": {
                "params": [
                    {
                        "key": "dt",
                        "value": "1703433877099"
                    },
                    {
                        "key": "flash",
                        "value": "0"
                    },
                    {
                        "key": "frm",
                        "value": "0"
                    },
                    {
                        "key": "u_tz",
                        "value": "180"
                    },
                    {
                        "key": "u_his",
                        "value": "50"
                    },
                    {
                        "key": "u_h",
                        "value": "864"
                    },
                    {
                        "key": "u_w",
                        "value": "1536"
                    },
                    {
                        "key": "u_ah",
                        "value": "824"
                    },
                    {
                        "key": "u_aw",
                        "value": "1536"
                    },
                    {
                        "key": "u_cd",
                        "value": "24"
                    },
                    {
                        "key": "bc",
                        "value": "31"
                    },
                    {
                        "key": "bih",
                        "value": "306"
                    },
                    {
                        "key": "biw",
                        "value": "1520"
                    },
                    {
                        "key": "brdim",
                        "value": "0,0,0,0,1536,0,1536,824,1536,306"
                    },
                    {
                        "key": "vis",
                        "value": "1"
                    },
                    {
                        "key": "wgl",
                        "value": "true"
                    },
                    {
                        "key": "ca_type",
                        "value": "image"
                    }
                ]
            }
        },
        "browseId": "FEwhat_to_watch",
        "inlineSettingStatus": "INLINE_SETTING_STATUS_ON"
    })
    headers = {
        'authority': 'www.youtube.com',
        'accept': '*/*',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/json',
        'cookie': 'CONSENT=PENDING+917; SOCS=CAISEwgDEgk1ODE3OTQxMTEaAnJ1IAEaBgiAlNCqBg; wide=1; _gcl_au=1.1.1236695019.1702128731; _ga=GA1.1.46170218.1702128973; PREF=f4=4000000&f6=40000000&tz=Europe.Moscow&f7=100&f5=30000&guide_collapsed=true; _ga_VCGEPY40VB=GS1.1.1702217844.6.0.1702217844.0.0.0; VISITOR_PRIVACY_METADATA=CgJERRIEEgAgOg%3D%3D; VISITOR_INFO1_LIVE=1uQAro3414g; YSC=mbg-Ztr7WdQ; GPS=1; ST-1b=itct=CB8Q8KgHGAAiEwijnIXbuaiDAxXRB9YAHdqdBAI%3D&csn=MC40MzgwNjk1MTM2MDc0OTg4&endpoint=%7B%22clickTrackingParams%22%3A%22CB8Q8KgHGAAiEwijnIXbuaiDAxXRB9YAHdqdBAI%3D%22%2C%22commandMetadata%22%3A%7B%22webCommandMetadata%22%3A%7B%22url%22%3A%22%2F%22%2C%22webPageType%22%3A%22WEB_PAGE_TYPE_BROWSE%22%2C%22rootVe%22%3A3854%2C%22apiUrl%22%3A%22%2Fyoutubei%2Fv1%2Fbrowse%22%7D%7D%2C%22browseEndpoint%22%3A%7B%22browseId%22%3A%22FEwhat_to_watch%22%7D%7D',
        'origin': 'https://www.youtube.com',
        'referer': 'https://www.youtube.com/',
        'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
        'sec-ch-ua-arch': '"x86"',
        'sec-ch-ua-bitness': '"64"',
        'sec-ch-ua-full-version': '"120.0.6099.129"',
        'sec-ch-ua-full-version-list': '"Not_A Brand";v="8.0.0.0", "Chromium";v="120.0.6099.129", "Google Chrome";v="120.0.6099.129"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-model': '""',
        'sec-ch-ua-platform': '"Windows"',
        'sec-ch-ua-platform-version': '"10.0.0"',
        'sec-ch-ua-wow64': '?0',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'same-origin',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'x-client-data': 'CKm1yQEIj7bJAQimtskBCKmdygEIhZbLAQiWocsBCJv+zAEI+ZjNAQiFoM0BCNy9zQEIj+HNAQiu6c0BCN7szQEIoe7NAQjJ7s0BCIPwzQEIhfDNARin6s0B',
        'x-goog-visitor-id': 'CgsxdVFBcm8zNDE0ZyiUraGsBjIKCgJERRIEEgAgOg%3D%3D',
        'x-youtube-bootstrap-logged-in': 'false',
        'x-youtube-client-name': '1',
        'x-youtube-client-version': '2.20231219.04.00'
    }
    return url, payload, headers
#
#
#
#
#


def check_left_menu_subscriptions_button_api():
    url = "https://www.youtube.com/youtubei/v1/browse?key=AIzaSyAO_FJ2SlqU8Q4STEHLGCilw_Y9_11qcW8&prettyPrint=false"

    payload = json.dumps({
        "context": {
            "client": {
                "hl": "ru",
                "gl": "GB",
                "remoteHost": "23.106.56.21",
                "deviceMake": "",
                "deviceModel": "",
                "visitorData": "CgsxdVFBcm8zNDE0ZyiO9aCsBjIKCgJERRIEEgAgOg%3D%3D",
                "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36,gzip(gfe)",
                "clientName": "WEB",
                "clientVersion": "2.20231219.04.00",
                "osName": "Windows",
                "osVersion": "10.0",
                "originalUrl": "https://www.youtube.com/feed/subscriptions",
                "screenPixelDensity": 1,
                "platform": "DESKTOP",
                "clientFormFactor": "UNKNOWN_FORM_FACTOR",
                "configInfo": {
                    "appInstallData": "CI71oKwGEOrDrwUQnouwBRCZkbAFENyCsAUQyfevBRD8hbAFEOeG_xIQ2piwBRDuoq8FENfprwUQvPmvBRCPorAFEPufsAUQieiuBRDd6P4SEKXC_hIQ-Z-wBRCrgrAFEJqksAUQ6-j-EhDSlbAFEKy3rwUQ57qvBRCmoLAFENShrwUQ5LP-EhCigbAFEKn3rwUQx4OwBRCa8K8FELfvrwUQ_Z-wBRDbr68FEKaasAUQt52wBRDMrv4SEKihsAUQ6YywBRC9mbAFEKSgsAUQuIuuBRDM364FEKiasAUQmPz-EhD1-a8FEJT6_hIQiIewBRD6krAFEOHyrwUQvvmvBRC9tq4FENPhrwUQ1YiwBRCikrAFEOuTrgUQ0I2wBRCI468FEOLUrgUQt-r-EhCpoLAFEL2KsAUQpoGwBRDNlbAFENnJrwUQmZSwBRCu1P4SEJeDsAUQ16SwBRCwpbAFEOaesAUQ5qOwBQ%3D%3D"
                },
                "screenDensityFloat": 1.25,
                "userInterfaceTheme": "USER_INTERFACE_THEME_DARK",
                "timeZone": "Europe/Moscow",
                "browserName": "Chrome",
                "browserVersion": "120.0.0.0",
                "acceptHeader": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                "deviceExperimentId": "ChxOek14TmpFMk1UazNOekl4TlRnMk5ERTRNdz09EI71oKwGGI71oKwG",
                "screenWidthPoints": 1536,
                "screenHeightPoints": 150,
                "utcOffsetMinutes": 180,
                "memoryTotalKbytes": "8000000",
                "mainAppWebInfo": {
                    "graftUrl": "/feed/subscriptions",
                    "pwaInstallabilityStatus": "PWA_INSTALLABILITY_STATUS_CAN_BE_INSTALLED",
                    "webDisplayMode": "WEB_DISPLAY_MODE_BROWSER",
                    "isWebNativeShareAvailable": True
                }
            },
            "user": {
                "lockedSafetyMode": False
            },
            "request": {
                "useSsl": True,
                "internalExperimentFlags": [],
                "consistencyTokenJars": []
            },
            "clickTracking": {
                "clickTrackingParams": "CBsQ8qgHGAIiEwi_m7j9nqiDAxX1HAYAHfU6BdA="
            },
            "adSignalsInfo": {
                "params": [
                    {
                        "key": "dt",
                        "value": "1703426703681"
                    },
                    {
                        "key": "flash",
                        "value": "0"
                    },
                    {
                        "key": "frm",
                        "value": "0"
                    },
                    {
                        "key": "u_tz",
                        "value": "180"
                    },
                    {
                        "key": "u_his",
                        "value": "50"
                    },
                    {
                        "key": "u_h",
                        "value": "864"
                    },
                    {
                        "key": "u_w",
                        "value": "1536"
                    },
                    {
                        "key": "u_ah",
                        "value": "824"
                    },
                    {
                        "key": "u_aw",
                        "value": "1536"
                    },
                    {
                        "key": "u_cd",
                        "value": "24"
                    },
                    {
                        "key": "bc",
                        "value": "31"
                    },
                    {
                        "key": "bih",
                        "value": "150"
                    },
                    {
                        "key": "biw",
                        "value": "1520"
                    },
                    {
                        "key": "brdim",
                        "value": "0,0,0,0,1536,0,1536,824,1536,150"
                    },
                    {
                        "key": "vis",
                        "value": "1"
                    },
                    {
                        "key": "wgl",
                        "value": "true"
                    },
                    {
                        "key": "ca_type",
                        "value": "image"
                    }
                ]
            }
        },
        "browseId": "FEsubscriptions"
    })
    headers = {
        'authority': 'www.youtube.com',
        'accept': '*/*',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/json',
        'cookie': 'CONSENT=PENDING+917; SOCS=CAISEwgDEgk1ODE3OTQxMTEaAnJ1IAEaBgiAlNCqBg; wide=1; _gcl_au=1.1.1236695019.1702128731; _ga=GA1.1.46170218.1702128973; PREF=f4=4000000&f6=40000000&tz=Europe.Moscow&f7=100&f5=30000&guide_collapsed=true; _ga_VCGEPY40VB=GS1.1.1702217844.6.0.1702217844.0.0.0; VISITOR_PRIVACY_METADATA=CgJERRIEEgAgOg%3D%3D; VISITOR_INFO1_LIVE=1uQAro3414g; YSC=mbg-Ztr7WdQ; GPS=1; ST-1tzw2b8=itct=CBsQ8qgHGAIiEwi_m7j9nqiDAxX1HAYAHfU6BdA%3D&csn=MC42MjEwMjI1MTYyODQ1MTE4&endpoint=%7B%22clickTrackingParams%22%3A%22CBsQ8qgHGAIiEwi_m7j9nqiDAxX1HAYAHfU6BdA%3D%22%2C%22commandMetadata%22%3A%7B%22webCommandMetadata%22%3A%7B%22url%22%3A%22%2Ffeed%2Fsubscriptions%22%2C%22webPageType%22%3A%22WEB_PAGE_TYPE_BROWSE%22%2C%22rootVe%22%3A96368%2C%22apiUrl%22%3A%22%2Fyoutubei%2Fv1%2Fbrowse%22%7D%7D%2C%22browseEndpoint%22%3A%7B%22browseId%22%3A%22FEsubscriptions%22%7D%7D',
        'origin': 'https://www.youtube.com',
        'referer': 'https://www.youtube.com/feed/subscriptions',
        'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
        'sec-ch-ua-arch': '"x86"',
        'sec-ch-ua-bitness': '"64"',
        'sec-ch-ua-full-version': '"120.0.6099.129"',
        'sec-ch-ua-full-version-list': '"Not_A Brand";v="8.0.0.0", "Chromium";v="120.0.6099.129", "Google Chrome";v="120.0.6099.129"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-model': '""',
        'sec-ch-ua-platform': '"Windows"',
        'sec-ch-ua-platform-version': '"10.0.0"',
        'sec-ch-ua-wow64': '?0',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'same-origin',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'x-client-data': 'CKm1yQEIj7bJAQimtskBCKmdygEIhZbLAQiWocsBCJv+zAEI+ZjNAQiFoM0BCNy9zQEIj+HNAQiu6c0BCN7szQEIoe7NAQjJ7s0BCIPwzQEIhfDNARin6s0B',
        'x-goog-visitor-id': 'CgsxdVFBcm8zNDE0ZyiO9aCsBjIKCgJERRIEEgAgOg%3D%3D',
        'x-youtube-bootstrap-logged-in': 'false',
        'x-youtube-client-name': '1',
        'x-youtube-client-version': '2.20231219.04.00'
    }
    return url, payload, headers
#
#
#
#
#


def check_left_menu_you_button_api():
    url = "https://www.youtube.com/youtubei/v1/browse?key=AIzaSyAO_FJ2SlqU8Q4STEHLGCilw_Y9_11qcW8&prettyPrint=false"

    payload = json.dumps({
        "context": {
            "client": {
                "hl": "ru",
                "gl": "US",
                "remoteHost": "207.244.71.81",
                "deviceMake": "",
                "deviceModel": "",
                "visitorData": "CgsxdVFBcm8zNDE0ZyjAuqGsBjIKCgJERRIEEgAgOg%3D%3D",
                "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36,gzip(gfe)",
                "clientName": "WEB",
                "clientVersion": "2.20231219.04.00",
                "osName": "Windows",
                "osVersion": "10.0",
                "originalUrl": "https://www.youtube.com/feed/you",
                "screenPixelDensity": 1,
                "platform": "DESKTOP",
                "clientFormFactor": "UNKNOWN_FORM_FACTOR",
                "configInfo": {
                    "appInstallData": "CMC6oawGEOuTrgUQ6sOvBRC8-a8FEKKBsAUQuIuuBRC--a8FEInorgUQzK7-EhCPorAFEP2fsAUQ26-vBRCU-v4SEJj8_hIQ9fmvBRDks_4SELfq_hIQ4fKvBRDd6P4SEMn3rwUQq4KwBRC9tq4FEL2KsAUQl4OwBRDr6P4SENfprwUQqKGwBRDM364FEKSgsAUQ4tSuBRDHg7AFEKy3rwUQ57qvBRDViLAFEO6irwUQmvCvBRCapLAFEPufsAUQt52wBRCZlLAFEPmfsAUQ3IKwBRC3768FEIjjrwUQnouwBRComrAFEKn3rwUQ0I2wBRDZya8FEKaasAUQpqCwBRDamLAFEPyFsAUQ0pWwBRDT4a8FEL2ZsAUQ6YywBRCmgbAFEJmRsAUQzZWwBRCpoLAFEKKSsAUQiIewBRD6krAFENShrwUQrtT-EhClwv4SEOeG_xIQ16SwBRDH_LciEOajsAUQ5p6wBRCwpbAF"
                },
                "screenDensityFloat": 1.25,
                "userInterfaceTheme": "USER_INTERFACE_THEME_DARK",
                "timeZone": "Europe/Moscow",
                "browserName": "Chrome",
                "browserVersion": "120.0.0.0",
                "acceptHeader": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                "deviceExperimentId": "ChxOek14TmpJd01ERXlOVFF5TWpBM01EUTFOdz09EMC6oawGGMC6oawG",
                "screenWidthPoints": 1536,
                "screenHeightPoints": 306,
                "utcOffsetMinutes": 180,
                "memoryTotalKbytes": "8000000",
                "mainAppWebInfo": {
                    "graftUrl": "/feed/you",
                    "pwaInstallabilityStatus": "PWA_INSTALLABILITY_STATUS_CAN_BE_INSTALLED",
                    "webDisplayMode": "WEB_DISPLAY_MODE_BROWSER",
                    "isWebNativeShareAvailable": True
                }
            },
            "user": {
                "lockedSafetyMode": False
            },
            "request": {
                "useSsl": True,
                "internalExperimentFlags": [],
                "consistencyTokenJars": []
            },
            "clickTracking": {
                "clickTrackingParams": "CBoQ8agHGAAiEwj6lsuJwKiDAxUKpsEKHaXOBD0="
            },
            "adSignalsInfo": {
                "params": [
                    {
                        "key": "dt",
                        "value": "1703435585740"
                    },
                    {
                        "key": "flash",
                        "value": "0"
                    },
                    {
                        "key": "frm",
                        "value": "0"
                    },
                    {
                        "key": "u_tz",
                        "value": "180"
                    },
                    {
                        "key": "u_his",
                        "value": "50"
                    },
                    {
                        "key": "u_h",
                        "value": "864"
                    },
                    {
                        "key": "u_w",
                        "value": "1536"
                    },
                    {
                        "key": "u_ah",
                        "value": "824"
                    },
                    {
                        "key": "u_aw",
                        "value": "1536"
                    },
                    {
                        "key": "u_cd",
                        "value": "24"
                    },
                    {
                        "key": "bc",
                        "value": "31"
                    },
                    {
                        "key": "bih",
                        "value": "306"
                    },
                    {
                        "key": "biw",
                        "value": "1520"
                    },
                    {
                        "key": "brdim",
                        "value": "0,0,0,0,1536,0,1536,824,1536,306"
                    },
                    {
                        "key": "vis",
                        "value": "1"
                    },
                    {
                        "key": "wgl",
                        "value": "true"
                    },
                    {
                        "key": "ca_type",
                        "value": "image"
                    }
                ]
            }
        },
        "browseId": "FElibrary",
        "params": "KgN5b3U%3D"
    })
    headers = {
        'authority': 'www.youtube.com',
        'accept': '*/*',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/json',
        'cookie': 'CONSENT=PENDING+917; SOCS=CAISEwgDEgk1ODE3OTQxMTEaAnJ1IAEaBgiAlNCqBg; wide=1; _gcl_au=1.1.1236695019.1702128731; _ga=GA1.1.46170218.1702128973; PREF=f4=4000000&f6=40000000&tz=Europe.Moscow&f7=100&f5=30000&guide_collapsed=true; _ga_VCGEPY40VB=GS1.1.1702217844.6.0.1702217844.0.0.0; VISITOR_PRIVACY_METADATA=CgJERRIEEgAgOg%3D%3D; VISITOR_INFO1_LIVE=1uQAro3414g; YSC=mbg-Ztr7WdQ; ST-ci3gpp=itct=CBoQ8agHGAAiEwj6lsuJwKiDAxUKpsEKHaXOBD0%3D&csn=MC40NzA3MzQ3MjYyODExNDE5&endpoint=%7B%22clickTrackingParams%22%3A%22CBoQ8agHGAAiEwj6lsuJwKiDAxUKpsEKHaXOBD0%3D%22%2C%22commandMetadata%22%3A%7B%22webCommandMetadata%22%3A%7B%22url%22%3A%22%2Ffeed%2Fyou%22%2C%22webPageType%22%3A%22WEB_PAGE_TYPE_BROWSE%22%2C%22rootVe%22%3A6827%2C%22apiUrl%22%3A%22%2Fyoutubei%2Fv1%2Fbrowse%22%7D%7D%2C%22browseEndpoint%22%3A%7B%22browseId%22%3A%22FElibrary%22%2C%22params%22%3A%22KgN5b3U%253D%22%7D%7D',
        'origin': 'https://www.youtube.com',
        'referer': 'https://www.youtube.com/feed/you',
        'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
        'sec-ch-ua-arch': '"x86"',
        'sec-ch-ua-bitness': '"64"',
        'sec-ch-ua-full-version': '"120.0.6099.129"',
        'sec-ch-ua-full-version-list': '"Not_A Brand";v="8.0.0.0", "Chromium";v="120.0.6099.129", "Google Chrome";v="120.0.6099.129"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-model': '""',
        'sec-ch-ua-platform': '"Windows"',
        'sec-ch-ua-platform-version': '"10.0.0"',
        'sec-ch-ua-wow64': '?0',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'same-origin',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'x-client-data': 'CKm1yQEIj7bJAQimtskBCKmdygEIhZbLAQiWocsBCJv+zAEI+ZjNAQiFoM0BCNy9zQEIj+HNAQiu6c0BCN7szQEIoe7NAQjJ7s0BCIPwzQEIhfDNARin6s0B',
        'x-goog-visitor-id': 'CgsxdVFBcm8zNDE0ZyjAuqGsBjIKCgJERRIEEgAgOg%3D%3D',
        'x-youtube-bootstrap-logged-in': 'false',
        'x-youtube-client-name': '1',
        'x-youtube-client-version': '2.20231219.04.00'
    }
    return url, payload, headers
#
#
#
#
#


def check_left_menu_history_button():
    url = "https://www.youtube.com/youtubei/v1/browse?key=AIzaSyAO_FJ2SlqU8Q4STEHLGCilw_Y9_11qcW8&prettyPrint=false"

    payload = json.dumps({
        "context": {
            "client": {
                "hl": "ru",
                "gl": "US",
                "remoteHost": "207.244.71.81",
                "deviceMake": "",
                "deviceModel": "",
                "visitorData": "CgsxdVFBcm8zNDE0ZyjAuqGsBjIKCgJERRIEEgAgOg%3D%3D",
                "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36,gzip(gfe)",
                "clientName": "WEB",
                "clientVersion": "2.20231219.04.00",
                "osName": "Windows",
                "osVersion": "10.0",
                "originalUrl": "https://www.youtube.com/feed/history",
                "screenPixelDensity": 1,
                "platform": "DESKTOP",
                "clientFormFactor": "UNKNOWN_FORM_FACTOR",
                "configInfo": {
                    "appInstallData": "CMC6oawGEOuTrgUQ6sOvBRC8-a8FEKKBsAUQuIuuBRC--a8FEInorgUQzK7-EhCPorAFEP2fsAUQ26-vBRCU-v4SEJj8_hIQ9fmvBRDks_4SELfq_hIQ4fKvBRDd6P4SEMn3rwUQq4KwBRC9tq4FEL2KsAUQl4OwBRDr6P4SENfprwUQqKGwBRDM364FEKSgsAUQ4tSuBRDHg7AFEKy3rwUQ57qvBRDViLAFEO6irwUQmvCvBRCapLAFEPufsAUQt52wBRCZlLAFEPmfsAUQ3IKwBRC3768FEIjjrwUQnouwBRComrAFEKn3rwUQ0I2wBRDZya8FEKaasAUQpqCwBRDamLAFEPyFsAUQ0pWwBRDT4a8FEL2ZsAUQ6YywBRCmgbAFEJmRsAUQzZWwBRCpoLAFEKKSsAUQiIewBRD6krAFENShrwUQrtT-EhClwv4SEOeG_xIQ16SwBRDH_LciEOajsAUQ5p6wBRCwpbAF"
                },
                "screenDensityFloat": 1.25,
                "userInterfaceTheme": "USER_INTERFACE_THEME_DARK",
                "timeZone": "Europe/Moscow",
                "browserName": "Chrome",
                "browserVersion": "120.0.0.0",
                "acceptHeader": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                "deviceExperimentId": "ChxOek14TmpJd01ERXlOVFF5TWpBM01EUTFOdz09EMC6oawGGMC6oawG",
                "screenWidthPoints": 1536,
                "screenHeightPoints": 306,
                "utcOffsetMinutes": 180,
                "memoryTotalKbytes": "8000000",
                "mainAppWebInfo": {
                    "graftUrl": "/feed/history",
                    "pwaInstallabilityStatus": "PWA_INSTALLABILITY_STATUS_CAN_BE_INSTALLED",
                    "webDisplayMode": "WEB_DISPLAY_MODE_BROWSER",
                    "isWebNativeShareAvailable": True
                }
            },
            "user": {
                "lockedSafetyMode": False
            },
            "request": {
                "useSsl": True,
                "internalExperimentFlags": [],
                "consistencyTokenJars": []
            },
            "clickTracking": {
                "clickTrackingParams": "CBkQ5KgHGAEiEwj6lsuJwKiDAxUKpsEKHaXOBD0="
            },
            "adSignalsInfo": {
                "params": [
                    {
                        "key": "dt",
                        "value": "1703435585740"
                    },
                    {
                        "key": "flash",
                        "value": "0"
                    },
                    {
                        "key": "frm",
                        "value": "0"
                    },
                    {
                        "key": "u_tz",
                        "value": "180"
                    },
                    {
                        "key": "u_his",
                        "value": "49"
                    },
                    {
                        "key": "u_h",
                        "value": "864"
                    },
                    {
                        "key": "u_w",
                        "value": "1536"
                    },
                    {
                        "key": "u_ah",
                        "value": "824"
                    },
                    {
                        "key": "u_aw",
                        "value": "1536"
                    },
                    {
                        "key": "u_cd",
                        "value": "24"
                    },
                    {
                        "key": "bc",
                        "value": "31"
                    },
                    {
                        "key": "bih",
                        "value": "306"
                    },
                    {
                        "key": "biw",
                        "value": "1520"
                    },
                    {
                        "key": "brdim",
                        "value": "0,0,0,0,1536,0,1536,824,1536,306"
                    },
                    {
                        "key": "vis",
                        "value": "1"
                    },
                    {
                        "key": "wgl",
                        "value": "true"
                    },
                    {
                        "key": "ca_type",
                        "value": "image"
                    }
                ]
            }
        },
        "browseId": "FEhistory"
    })
    headers = {
        'authority': 'www.youtube.com',
        'accept': '*/*',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/json',
        'cookie': 'CONSENT=PENDING+917; SOCS=CAISEwgDEgk1ODE3OTQxMTEaAnJ1IAEaBgiAlNCqBg; wide=1; _gcl_au=1.1.1236695019.1702128731; _ga=GA1.1.46170218.1702128973; PREF=f4=4000000&f6=40000000&tz=Europe.Moscow&f7=100&f5=30000&guide_collapsed=true; _ga_VCGEPY40VB=GS1.1.1702217844.6.0.1702217844.0.0.0; VISITOR_PRIVACY_METADATA=CgJERRIEEgAgOg%3D%3D; VISITOR_INFO1_LIVE=1uQAro3414g; YSC=mbg-Ztr7WdQ; ST-cv3kr6=itct=CBkQ5KgHGAEiEwj6lsuJwKiDAxUKpsEKHaXOBD0%3D&csn=MC40NjM2MjQ3ODMzOTQyNDc1&endpoint=%7B%22clickTrackingParams%22%3A%22CBkQ5KgHGAEiEwj6lsuJwKiDAxUKpsEKHaXOBD0%3D%22%2C%22commandMetadata%22%3A%7B%22webCommandMetadata%22%3A%7B%22url%22%3A%22%2Ffeed%2Fhistory%22%2C%22webPageType%22%3A%22WEB_PAGE_TYPE_BROWSE%22%2C%22rootVe%22%3A6827%2C%22apiUrl%22%3A%22%2Fyoutubei%2Fv1%2Fbrowse%22%7D%7D%2C%22browseEndpoint%22%3A%7B%22browseId%22%3A%22FEhistory%22%7D%7D',
        'origin': 'https://www.youtube.com',
        'referer': 'https://www.youtube.com/feed/history',
        'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
        'sec-ch-ua-arch': '"x86"',
        'sec-ch-ua-bitness': '"64"',
        'sec-ch-ua-full-version': '"120.0.6099.129"',
        'sec-ch-ua-full-version-list': '"Not_A Brand";v="8.0.0.0", "Chromium";v="120.0.6099.129", "Google Chrome";v="120.0.6099.129"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-model': '""',
        'sec-ch-ua-platform': '"Windows"',
        'sec-ch-ua-platform-version': '"10.0.0"',
        'sec-ch-ua-wow64': '?0',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'same-origin',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'x-client-data': 'CKm1yQEIj7bJAQimtskBCKmdygEIhZbLAQiWocsBCJv+zAEI+ZjNAQiFoM0BCNy9zQEIj+HNAQiu6c0BCN7szQEIoe7NAQjJ7s0BCIPwzQEIhfDNARin6s0B',
        'x-goog-visitor-id': 'CgsxdVFBcm8zNDE0ZyjAuqGsBjIKCgJERRIEEgAgOg%3D%3D',
        'x-youtube-bootstrap-logged-in': 'false',
        'x-youtube-client-name': '1',
        'x-youtube-client-version': '2.20231219.04.00'
    }
    return url, payload, headers
#
#
#
#
#


def check_left_menu_trend_button_api():
    url = "https://www.youtube.com/youtubei/v1/browse?key=AIzaSyAO_FJ2SlqU8Q4STEHLGCilw_Y9_11qcW8&prettyPrint=false"

    payload = json.dumps({
        "context": {
            "client": {
                "hl": "ru",
                "gl": "US",
                "remoteHost": "207.244.71.81",
                "deviceMake": "",
                "deviceModel": "",
                "visitorData": "CgsxdVFBcm8zNDE0ZyjAuqGsBjIKCgJERRIEEgAgOg%3D%3D",
                "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36,gzip(gfe)",
                "clientName": "WEB",
                "clientVersion": "2.20231219.04.00",
                "osName": "Windows",
                "osVersion": "10.0",
                "originalUrl": "https://www.youtube.com/feed/trending?bp=6gQJRkVleHBsb3Jl",
                "screenPixelDensity": 1,
                "platform": "DESKTOP",
                "clientFormFactor": "UNKNOWN_FORM_FACTOR",
                "configInfo": {
                    "appInstallData": "CMC6oawGEOuTrgUQ6sOvBRC8-a8FEKKBsAUQuIuuBRC--a8FEInorgUQzK7-EhCPorAFEP2fsAUQ26-vBRCU-v4SEJj8_hIQ9fmvBRDks_4SELfq_hIQ4fKvBRDd6P4SEMn3rwUQq4KwBRC9tq4FEL2KsAUQl4OwBRDr6P4SENfprwUQqKGwBRDM364FEKSgsAUQ4tSuBRDHg7AFEKy3rwUQ57qvBRDViLAFEO6irwUQmvCvBRCapLAFEPufsAUQt52wBRCZlLAFEPmfsAUQ3IKwBRC3768FEIjjrwUQnouwBRComrAFEKn3rwUQ0I2wBRDZya8FEKaasAUQpqCwBRDamLAFEPyFsAUQ0pWwBRDT4a8FEL2ZsAUQ6YywBRCmgbAFEJmRsAUQzZWwBRCpoLAFEKKSsAUQiIewBRD6krAFENShrwUQrtT-EhClwv4SEOeG_xIQ16SwBRDH_LciEOajsAUQ5p6wBRCwpbAF"
                },
                "screenDensityFloat": 1.25,
                "userInterfaceTheme": "USER_INTERFACE_THEME_DARK",
                "timeZone": "Europe/Moscow",
                "browserName": "Chrome",
                "browserVersion": "120.0.0.0",
                "acceptHeader": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                "deviceExperimentId": "ChxOek14TmpJd01ERXlOVFF5TWpBM01EUTFOdz09EMC6oawGGMC6oawG",
                "screenWidthPoints": 1536,
                "screenHeightPoints": 306,
                "utcOffsetMinutes": 180,
                "memoryTotalKbytes": "8000000",
                "mainAppWebInfo": {
                    "graftUrl": "/feed/trending?bp=6gQJRkVleHBsb3Jl",
                    "pwaInstallabilityStatus": "PWA_INSTALLABILITY_STATUS_CAN_BE_INSTALLED",
                    "webDisplayMode": "WEB_DISPLAY_MODE_BROWSER",
                    "isWebNativeShareAvailable": True
                }
            },
            "user": {
                "lockedSafetyMode": False
            },
            "request": {
                "useSsl": True,
                "internalExperimentFlags": [],
                "consistencyTokenJars": []
            },
            "clickTracking": {
                "clickTrackingParams": "CBYQv54JGAAiEwj6lsuJwKiDAxUKpsEKHaXOBD0="
            },
            "adSignalsInfo": {
                "params": [
                    {
                        "key": "dt",
                        "value": "1703435585740"
                    },
                    {
                        "key": "flash",
                        "value": "0"
                    },
                    {
                        "key": "frm",
                        "value": "0"
                    },
                    {
                        "key": "u_tz",
                        "value": "180"
                    },
                    {
                        "key": "u_his",
                        "value": "50"
                    },
                    {
                        "key": "u_h",
                        "value": "864"
                    },
                    {
                        "key": "u_w",
                        "value": "1536"
                    },
                    {
                        "key": "u_ah",
                        "value": "824"
                    },
                    {
                        "key": "u_aw",
                        "value": "1536"
                    },
                    {
                        "key": "u_cd",
                        "value": "24"
                    },
                    {
                        "key": "bc",
                        "value": "31"
                    },
                    {
                        "key": "bih",
                        "value": "306"
                    },
                    {
                        "key": "biw",
                        "value": "1520"
                    },
                    {
                        "key": "brdim",
                        "value": "0,0,0,0,1536,0,1536,824,1536,306"
                    },
                    {
                        "key": "vis",
                        "value": "1"
                    },
                    {
                        "key": "wgl",
                        "value": "true"
                    },
                    {
                        "key": "ca_type",
                        "value": "image"
                    }
                ]
            }
        },
        "browseId": "FEtrending",
        "params": "6gQJRkVleHBsb3Jl"
    })
    headers = {
        'authority': 'www.youtube.com',
        'accept': '*/*',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/json',
        'cookie': 'CONSENT=PENDING+917; SOCS=CAISEwgDEgk1ODE3OTQxMTEaAnJ1IAEaBgiAlNCqBg; wide=1; _gcl_au=1.1.1236695019.1702128731; _ga=GA1.1.46170218.1702128973; PREF=f4=4000000&f6=40000000&tz=Europe.Moscow&f7=100&f5=30000&guide_collapsed=true; _ga_VCGEPY40VB=GS1.1.1702217844.6.0.1702217844.0.0.0; VISITOR_PRIVACY_METADATA=CgJERRIEEgAgOg%3D%3D; VISITOR_INFO1_LIVE=1uQAro3414g; YSC=mbg-Ztr7WdQ; ST-1o03zo7=itct=CBYQv54JGAAiEwj6lsuJwKiDAxUKpsEKHaXOBD0%3D&csn=MC4zMTIyNjc0Mjc4NDA4NTIxNQ..&endpoint=%7B%22clickTrackingParams%22%3A%22CBYQv54JGAAiEwj6lsuJwKiDAxUKpsEKHaXOBD0%3D%22%2C%22commandMetadata%22%3A%7B%22webCommandMetadata%22%3A%7B%22url%22%3A%22%2Ffeed%2Ftrending%3Fbp%3D6gQJRkVleHBsb3Jl%22%2C%22webPageType%22%3A%22WEB_PAGE_TYPE_BROWSE%22%2C%22rootVe%22%3A6827%2C%22apiUrl%22%3A%22%2Fyoutubei%2Fv1%2Fbrowse%22%7D%7D%2C%22browseEndpoint%22%3A%7B%22browseId%22%3A%22FEtrending%22%2C%22params%22%3A%226gQJRkVleHBsb3Jl%22%7D%7D',
        'origin': 'https://www.youtube.com',
        'referer': 'https://www.youtube.com/feed/trending?bp=6gQJRkVleHBsb3Jl',
        'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
        'sec-ch-ua-arch': '"x86"',
        'sec-ch-ua-bitness': '"64"',
        'sec-ch-ua-full-version': '"120.0.6099.129"',
        'sec-ch-ua-full-version-list': '"Not_A Brand";v="8.0.0.0", "Chromium";v="120.0.6099.129", "Google Chrome";v="120.0.6099.129"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-model': '""',
        'sec-ch-ua-platform': '"Windows"',
        'sec-ch-ua-platform-version': '"10.0.0"',
        'sec-ch-ua-wow64': '?0',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'same-origin',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'x-client-data': 'CKm1yQEIj7bJAQimtskBCKmdygEIhZbLAQiWocsBCJv+zAEI+ZjNAQiFoM0BCNy9zQEIj+HNAQiu6c0BCN7szQEIoe7NAQjJ7s0BCIPwzQEIhfDNARin6s0B',
        'x-goog-visitor-id': 'CgsxdVFBcm8zNDE0ZyjAuqGsBjIKCgJERRIEEgAgOg%3D%3D',
        'x-youtube-bootstrap-logged-in': 'false',
        'x-youtube-client-name': '1',
        'x-youtube-client-version': '2.20231219.04.00'
    }
    return url, payload, headers
#
#
#
#
#


def check_left_menu_music_button_api():
    url = "https://www.youtube.com/youtubei/v1/browse?key=AIzaSyAO_FJ2SlqU8Q4STEHLGCilw_Y9_11qcW8&prettyPrint=false"

    payload = json.dumps({
        "context": {
            "client": {
                "hl": "ru",
                "gl": "US",
                "remoteHost": "207.244.71.81",
                "deviceMake": "",
                "deviceModel": "",
                "visitorData": "CgsxdVFBcm8zNDE0ZyjAuqGsBjIKCgJERRIEEgAgOg%3D%3D",
                "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36,gzip(gfe)",
                "clientName": "WEB",
                "clientVersion": "2.20231219.04.00",
                "osName": "Windows",
                "osVersion": "10.0",
                "originalUrl": "https://www.youtube.com/channel/UC-9-kyTW8ZkZNDHQJ6FgpwQ",
                "screenPixelDensity": 1,
                "platform": "DESKTOP",
                "clientFormFactor": "UNKNOWN_FORM_FACTOR",
                "configInfo": {
                    "appInstallData": "CMC6oawGEOuTrgUQ6sOvBRC8-a8FEKKBsAUQuIuuBRC--a8FEInorgUQzK7-EhCPorAFEP2fsAUQ26-vBRCU-v4SEJj8_hIQ9fmvBRDks_4SELfq_hIQ4fKvBRDd6P4SEMn3rwUQq4KwBRC9tq4FEL2KsAUQl4OwBRDr6P4SENfprwUQqKGwBRDM364FEKSgsAUQ4tSuBRDHg7AFEKy3rwUQ57qvBRDViLAFEO6irwUQmvCvBRCapLAFEPufsAUQt52wBRCZlLAFEPmfsAUQ3IKwBRC3768FEIjjrwUQnouwBRComrAFEKn3rwUQ0I2wBRDZya8FEKaasAUQpqCwBRDamLAFEPyFsAUQ0pWwBRDT4a8FEL2ZsAUQ6YywBRCmgbAFEJmRsAUQzZWwBRCpoLAFEKKSsAUQiIewBRD6krAFENShrwUQrtT-EhClwv4SEOeG_xIQ16SwBRDH_LciEOajsAUQ5p6wBRCwpbAF"
                },
                "screenDensityFloat": 1.25,
                "userInterfaceTheme": "USER_INTERFACE_THEME_DARK",
                "timeZone": "Europe/Moscow",
                "browserName": "Chrome",
                "browserVersion": "120.0.0.0",
                "acceptHeader": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                "deviceExperimentId": "ChxOek14TmpJd01ERXlOVFF5TWpBM01EUTFOdz09EMC6oawGGMC6oawG",
                "screenWidthPoints": 1536,
                "screenHeightPoints": 306,
                "utcOffsetMinutes": 180,
                "memoryTotalKbytes": "8000000",
                "mainAppWebInfo": {
                    "graftUrl": "/channel/UC-9-kyTW8ZkZNDHQJ6FgpwQ",
                    "pwaInstallabilityStatus": "PWA_INSTALLABILITY_STATUS_CAN_BE_INSTALLED",
                    "webDisplayMode": "WEB_DISPLAY_MODE_BROWSER",
                    "isWebNativeShareAvailable": True
                }
            },
            "user": {
                "lockedSafetyMode": False
            },
            "request": {
                "useSsl": True,
                "internalExperimentFlags": [],
                "consistencyTokenJars": []
            },
            "clickTracking": {
                "clickTrackingParams": "CBUQp4EJGAEiEwj6lsuJwKiDAxUKpsEKHaXOBD0="
            },
            "adSignalsInfo": {
                "params": [
                    {
                        "key": "dt",
                        "value": "1703435585740"
                    },
                    {
                        "key": "flash",
                        "value": "0"
                    },
                    {
                        "key": "frm",
                        "value": "0"
                    },
                    {
                        "key": "u_tz",
                        "value": "180"
                    },
                    {
                        "key": "u_his",
                        "value": "50"
                    },
                    {
                        "key": "u_h",
                        "value": "864"
                    },
                    {
                        "key": "u_w",
                        "value": "1536"
                    },
                    {
                        "key": "u_ah",
                        "value": "824"
                    },
                    {
                        "key": "u_aw",
                        "value": "1536"
                    },
                    {
                        "key": "u_cd",
                        "value": "24"
                    },
                    {
                        "key": "bc",
                        "value": "31"
                    },
                    {
                        "key": "bih",
                        "value": "306"
                    },
                    {
                        "key": "biw",
                        "value": "1520"
                    },
                    {
                        "key": "brdim",
                        "value": "0,0,0,0,1536,0,1536,824,1536,306"
                    },
                    {
                        "key": "vis",
                        "value": "1"
                    },
                    {
                        "key": "wgl",
                        "value": "true"
                    },
                    {
                        "key": "ca_type",
                        "value": "image"
                    }
                ]
            }
        },
        "browseId": "UC-9-kyTW8ZkZNDHQJ6FgpwQ"
    })
    headers = {
        'authority': 'www.youtube.com',
        'accept': '*/*',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/json',
        'cookie': 'CONSENT=PENDING+917; SOCS=CAISEwgDEgk1ODE3OTQxMTEaAnJ1IAEaBgiAlNCqBg; wide=1; _gcl_au=1.1.1236695019.1702128731; _ga=GA1.1.46170218.1702128973; PREF=f4=4000000&f6=40000000&tz=Europe.Moscow&f7=100&f5=30000&guide_collapsed=true; _ga_VCGEPY40VB=GS1.1.1702217844.6.0.1702217844.0.0.0; VISITOR_PRIVACY_METADATA=CgJERRIEEgAgOg%3D%3D; VISITOR_INFO1_LIVE=1uQAro3414g; YSC=mbg-Ztr7WdQ; ST-17pm9r8=itct=CBUQp4EJGAEiEwj6lsuJwKiDAxUKpsEKHaXOBD0%3D&csn=MC40NzQwNTc4MjI2MzAzMTcxNQ..&endpoint=%7B%22clickTrackingParams%22%3A%22CBUQp4EJGAEiEwj6lsuJwKiDAxUKpsEKHaXOBD0%3D%22%2C%22commandMetadata%22%3A%7B%22webCommandMetadata%22%3A%7B%22url%22%3A%22%2Fchannel%2FUC-9-kyTW8ZkZNDHQJ6FgpwQ%22%2C%22webPageType%22%3A%22WEB_PAGE_TYPE_CHANNEL%22%2C%22rootVe%22%3A3611%2C%22apiUrl%22%3A%22%2Fyoutubei%2Fv1%2Fbrowse%22%7D%7D%2C%22browseEndpoint%22%3A%7B%22browseId%22%3A%22UC-9-kyTW8ZkZNDHQJ6FgpwQ%22%7D%7D',
        'origin': 'https://www.youtube.com',
        'referer': 'https://www.youtube.com/channel/UC-9-kyTW8ZkZNDHQJ6FgpwQ',
        'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
        'sec-ch-ua-arch': '"x86"',
        'sec-ch-ua-bitness': '"64"',
        'sec-ch-ua-full-version': '"120.0.6099.129"',
        'sec-ch-ua-full-version-list': '"Not_A Brand";v="8.0.0.0", "Chromium";v="120.0.6099.129", "Google Chrome";v="120.0.6099.129"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-model': '""',
        'sec-ch-ua-platform': '"Windows"',
        'sec-ch-ua-platform-version': '"10.0.0"',
        'sec-ch-ua-wow64': '?0',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'same-origin',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'x-client-data': 'CKm1yQEIj7bJAQimtskBCKmdygEIhZbLAQiWocsBCJv+zAEI+ZjNAQiFoM0BCNy9zQEIj+HNAQiu6c0BCN7szQEIoe7NAQjJ7s0BCIPwzQEIhfDNARin6s0B',
        'x-goog-visitor-id': 'CgsxdVFBcm8zNDE0ZyjAuqGsBjIKCgJERRIEEgAgOg%3D%3D',
        'x-youtube-bootstrap-logged-in': 'false',
        'x-youtube-client-name': '1',
        'x-youtube-client-version': '2.20231219.04.00'
    }
    return url, payload, headers
#
#
#
#
#


def check_left_menu_video_games_button_api():
    url = "https://www.youtube.com/youtubei/v1/browse?key=AIzaSyAO_FJ2SlqU8Q4STEHLGCilw_Y9_11qcW8&prettyPrint=false"

    payload = json.dumps({
        "context": {
            "client": {
                "hl": "ru",
                "gl": "US",
                "remoteHost": "207.244.71.81",
                "deviceMake": "",
                "deviceModel": "",
                "visitorData": "CgsxdVFBcm8zNDE0ZyjGmqKsBjIKCgJERRIEEgAgOg%3D%3D",
                "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36,gzip(gfe)",
                "clientName": "WEB",
                "clientVersion": "2.20231219.04.00",
                "osName": "Windows",
                "osVersion": "10.0",
                "originalUrl": "https://www.youtube.com/gaming",
                "screenPixelDensity": 1,
                "platform": "DESKTOP",
                "clientFormFactor": "UNKNOWN_FORM_FACTOR",
                "configInfo": {
                    "appInstallData": "CMaaoqwGEMn3rwUQt52wBRCu1P4SEJT6_hIQ26-vBRDT4a8FEOvo_hIQmZSwBRDM364FEJqksAUQpcL-EhC36v4SEOrDrwUQ4tSuBRC--a8FEOeG_xIQ5LP-EhDcgrAFEMeDsAUQ2cmvBRCIh7AFEKaasAUQqaCwBRCZkbAFEL22rgUQ65OuBRDQjbAFEOe6rwUQooGwBRCei7AFEN3o_hIQj6KwBRCoobAFEOmMsAUQopKwBRCrgrAFEKn3rwUQmvCvBRD9n7AFEPufsAUQuIuuBRD1-a8FENfprwUQ-Z-wBRDMrv4SEJeDsAUQ1KGvBRDuoq8FEKy3rwUQzZWwBRD6krAFENWIsAUQ2piwBRCmoLAFEKSgsAUQvYqwBRC3768FEInorgUQvZmwBRCY_P4SEIjjrwUQ_IWwBRDSlbAFEKiasAUQ4fKvBRC8-a8FEKaBsAUQyPy3IhDXpLAFEOaesAUQsKWwBRDmo7AF"
                },
                "screenDensityFloat": 1.25,
                "userInterfaceTheme": "USER_INTERFACE_THEME_DARK",
                "timeZone": "Europe/Moscow",
                "browserName": "Chrome",
                "browserVersion": "120.0.0.0",
                "acceptHeader": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                "deviceExperimentId": "ChxOek14TmpJMU1qa3lOamt4T0RneE56Y3hOZz09EMaaoqwGGMaaoqwG",
                "screenWidthPoints": 1536,
                "screenHeightPoints": 434,
                "utcOffsetMinutes": 180,
                "memoryTotalKbytes": "8000000",
                "mainAppWebInfo": {
                    "graftUrl": "/gaming",
                    "pwaInstallabilityStatus": "PWA_INSTALLABILITY_STATUS_CAN_BE_INSTALLED",
                    "webDisplayMode": "WEB_DISPLAY_MODE_BROWSER",
                    "isWebNativeShareAvailable": True
                }
            },
            "user": {
                "lockedSafetyMode": False
            },
            "request": {
                "useSsl": True,
                "internalExperimentFlags": [],
                "consistencyTokenJars": []
            },
            "clickTracking": {
                "clickTrackingParams": "CBIQpIEJGAQiEwjjkI3x7aiDAxUGHdYAHSBTC-c="
            },
            "adSignalsInfo": {
                "params": [
                    {
                        "key": "dt",
                        "value": "1703447881561"
                    },
                    {
                        "key": "flash",
                        "value": "0"
                    },
                    {
                        "key": "frm",
                        "value": "0"
                    },
                    {
                        "key": "u_tz",
                        "value": "180"
                    },
                    {
                        "key": "u_his",
                        "value": "50"
                    },
                    {
                        "key": "u_h",
                        "value": "864"
                    },
                    {
                        "key": "u_w",
                        "value": "1536"
                    },
                    {
                        "key": "u_ah",
                        "value": "824"
                    },
                    {
                        "key": "u_aw",
                        "value": "1536"
                    },
                    {
                        "key": "u_cd",
                        "value": "24"
                    },
                    {
                        "key": "bc",
                        "value": "31"
                    },
                    {
                        "key": "bih",
                        "value": "434"
                    },
                    {
                        "key": "biw",
                        "value": "1519"
                    },
                    {
                        "key": "brdim",
                        "value": "0,0,0,0,1536,0,1536,824,1536,434"
                    },
                    {
                        "key": "vis",
                        "value": "1"
                    },
                    {
                        "key": "wgl",
                        "value": "true"
                    },
                    {
                        "key": "ca_type",
                        "value": "image"
                    }
                ]
            }
        },
        "browseId": "UCOpNcN46UbXVtpKMrmU4Abg"
    })
    headers = {
        'authority': 'www.youtube.com',
        'accept': '*/*',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/json',
        'cookie': 'CONSENT=PENDING+917; SOCS=CAISEwgDEgk1ODE3OTQxMTEaAnJ1IAEaBgiAlNCqBg; wide=1; _gcl_au=1.1.1236695019.1702128731; _ga=GA1.1.46170218.1702128973; PREF=f4=4000000&f6=40000000&tz=Europe.Moscow&f7=100&f5=30000&guide_collapsed=true; _ga_VCGEPY40VB=GS1.1.1702217844.6.0.1702217844.0.0.0; VISITOR_PRIVACY_METADATA=CgJERRIEEgAgOg%3D%3D; VISITOR_INFO1_LIVE=1uQAro3414g; YSC=mbg-Ztr7WdQ; GPS=1; ST-tuhr1a=itct=CBIQpIEJGAQiEwjjkI3x7aiDAxUGHdYAHSBTC-c%3D&csn=MC4yNzIzMDQ2MzEzMDY3NzYz&endpoint=%7B%22clickTrackingParams%22%3A%22CBIQpIEJGAQiEwjjkI3x7aiDAxUGHdYAHSBTC-c%3D%22%2C%22commandMetadata%22%3A%7B%22webCommandMetadata%22%3A%7B%22url%22%3A%22%2Fgaming%22%2C%22webPageType%22%3A%22WEB_PAGE_TYPE_CHANNEL%22%2C%22rootVe%22%3A3611%2C%22apiUrl%22%3A%22%2Fyoutubei%2Fv1%2Fbrowse%22%7D%7D%2C%22browseEndpoint%22%3A%7B%22browseId%22%3A%22UCOpNcN46UbXVtpKMrmU4Abg%22%7D%7D',
        'origin': 'https://www.youtube.com',
        'referer': 'https://www.youtube.com/gaming',
        'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
        'sec-ch-ua-arch': '"x86"',
        'sec-ch-ua-bitness': '"64"',
        'sec-ch-ua-full-version': '"120.0.6099.129"',
        'sec-ch-ua-full-version-list': '"Not_A Brand";v="8.0.0.0", "Chromium";v="120.0.6099.129", "Google Chrome";v="120.0.6099.129"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-model': '""',
        'sec-ch-ua-platform': '"Windows"',
        'sec-ch-ua-platform-version': '"10.0.0"',
        'sec-ch-ua-wow64': '?0',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'same-origin',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'x-client-data': 'CKm1yQEIj7bJAQimtskBCKmdygEIhZbLAQiWocsBCJv+zAEI+ZjNAQiFoM0BCNy9zQEIj+HNAQiu6c0BCN7szQEIoe7NAQjJ7s0BCIPwzQEIhfDNARin6s0B',
        'x-goog-visitor-id': 'CgsxdVFBcm8zNDE0ZyjGmqKsBjIKCgJERRIEEgAgOg%3D%3D',
        'x-youtube-bootstrap-logged-in': 'false',
        'x-youtube-client-name': '1',
        'x-youtube-client-version': '2.20231219.04.00'
    }
    return url, payload, headers
#
#
#
#
#


def check_left_menu_sport_button_api():
    url = "https://www.youtube.com/youtubei/v1/browse?key=AIzaSyAO_FJ2SlqU8Q4STEHLGCilw_Y9_11qcW8&prettyPrint=false"

    payload = json.dumps({
        "context": {
            "client": {
                "hl": "ru",
                "gl": "US",
                "remoteHost": "207.244.71.81",
                "deviceMake": "",
                "deviceModel": "",
                "visitorData": "CgsxdVFBcm8zNDE0ZyjGmqKsBjIKCgJERRIEEgAgOg%3D%3D",
                "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36,gzip(gfe)",
                "clientName": "WEB",
                "clientVersion": "2.20231219.04.00",
                "osName": "Windows",
                "osVersion": "10.0",
                "originalUrl": "https://www.youtube.com/channel/UCEgdi0XIXXZ-qJOFPf4JSKw",
                "screenPixelDensity": 1,
                "platform": "DESKTOP",
                "clientFormFactor": "UNKNOWN_FORM_FACTOR",
                "configInfo": {
                    "appInstallData": "CMaaoqwGEMn3rwUQt52wBRCu1P4SEJT6_hIQ26-vBRDT4a8FEOvo_hIQmZSwBRDM364FEJqksAUQpcL-EhC36v4SEOrDrwUQ4tSuBRC--a8FEOeG_xIQ5LP-EhDcgrAFEMeDsAUQ2cmvBRCIh7AFEKaasAUQqaCwBRCZkbAFEL22rgUQ65OuBRDQjbAFEOe6rwUQooGwBRCei7AFEN3o_hIQj6KwBRCoobAFEOmMsAUQopKwBRCrgrAFEKn3rwUQmvCvBRD9n7AFEPufsAUQuIuuBRD1-a8FENfprwUQ-Z-wBRDMrv4SEJeDsAUQ1KGvBRDuoq8FEKy3rwUQzZWwBRD6krAFENWIsAUQ2piwBRCmoLAFEKSgsAUQvYqwBRC3768FEInorgUQvZmwBRCY_P4SEIjjrwUQ_IWwBRDSlbAFEKiasAUQ4fKvBRC8-a8FEKaBsAUQyPy3IhDXpLAFEOaesAUQsKWwBRDmo7AF"
                },
                "screenDensityFloat": 1.25,
                "userInterfaceTheme": "USER_INTERFACE_THEME_DARK",
                "timeZone": "Europe/Moscow",
                "browserName": "Chrome",
                "browserVersion": "120.0.0.0",
                "acceptHeader": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                "deviceExperimentId": "ChxOek14TmpJMU1qa3lOamt4T0RneE56Y3hOZz09EMaaoqwGGMaaoqwG",
                "screenWidthPoints": 1536,
                "screenHeightPoints": 260,
                "utcOffsetMinutes": 180,
                "memoryTotalKbytes": "8000000",
                "mainAppWebInfo": {
                    "graftUrl": "/channel/UCEgdi0XIXXZ-qJOFPf4JSKw",
                    "pwaInstallabilityStatus": "PWA_INSTALLABILITY_STATUS_CAN_BE_INSTALLED",
                    "webDisplayMode": "WEB_DISPLAY_MODE_BROWSER",
                    "isWebNativeShareAvailable": True
                }
            },
            "user": {
                "lockedSafetyMode": False
            },
            "request": {
                "useSsl": True,
                "internalExperimentFlags": [],
                "consistencyTokenJars": []
            },
            "clickTracking": {
                "clickTrackingParams": "CBAQqoEJGAYiEwjjkI3x7aiDAxUGHdYAHSBTC-c="
            },
            "adSignalsInfo": {
                "params": [
                    {
                        "key": "dt",
                        "value": "1703447881561"
                    },
                    {
                        "key": "flash",
                        "value": "0"
                    },
                    {
                        "key": "frm",
                        "value": "0"
                    },
                    {
                        "key": "u_tz",
                        "value": "180"
                    },
                    {
                        "key": "u_his",
                        "value": "50"
                    },
                    {
                        "key": "u_h",
                        "value": "864"
                    },
                    {
                        "key": "u_w",
                        "value": "1536"
                    },
                    {
                        "key": "u_ah",
                        "value": "824"
                    },
                    {
                        "key": "u_aw",
                        "value": "1536"
                    },
                    {
                        "key": "u_cd",
                        "value": "24"
                    },
                    {
                        "key": "bc",
                        "value": "31"
                    },
                    {
                        "key": "bih",
                        "value": "260"
                    },
                    {
                        "key": "biw",
                        "value": "1519"
                    },
                    {
                        "key": "brdim",
                        "value": "0,0,0,0,1536,0,1536,824,1536,260"
                    },
                    {
                        "key": "vis",
                        "value": "1"
                    },
                    {
                        "key": "wgl",
                        "value": "true"
                    },
                    {
                        "key": "ca_type",
                        "value": "image"
                    }
                ]
            }
        },
        "browseId": "UCEgdi0XIXXZ-qJOFPf4JSKw"
    })
    headers = {
        'authority': 'www.youtube.com',
        'accept': '*/*',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/json',
        'cookie': 'CONSENT=PENDING+917; SOCS=CAISEwgDEgk1ODE3OTQxMTEaAnJ1IAEaBgiAlNCqBg; wide=1; _gcl_au=1.1.1236695019.1702128731; _ga=GA1.1.46170218.1702128973; PREF=f4=4000000&f6=40000000&tz=Europe.Moscow&f7=100&f5=30000&guide_collapsed=true; _ga_VCGEPY40VB=GS1.1.1702217844.6.0.1702217844.0.0.0; VISITOR_PRIVACY_METADATA=CgJERRIEEgAgOg%3D%3D; VISITOR_INFO1_LIVE=1uQAro3414g; YSC=mbg-Ztr7WdQ; GPS=1; ST-1qtitb=itct=CBAQqoEJGAYiEwjjkI3x7aiDAxUGHdYAHSBTC-c%3D&csn=MC41OTcxMzY0MDc1Mzc4NzQy&endpoint=%7B%22clickTrackingParams%22%3A%22CBAQqoEJGAYiEwjjkI3x7aiDAxUGHdYAHSBTC-c%3D%22%2C%22commandMetadata%22%3A%7B%22webCommandMetadata%22%3A%7B%22url%22%3A%22%2Fchannel%2FUCEgdi0XIXXZ-qJOFPf4JSKw%22%2C%22webPageType%22%3A%22WEB_PAGE_TYPE_CHANNEL%22%2C%22rootVe%22%3A3611%2C%22apiUrl%22%3A%22%2Fyoutubei%2Fv1%2Fbrowse%22%7D%7D%2C%22browseEndpoint%22%3A%7B%22browseId%22%3A%22UCEgdi0XIXXZ-qJOFPf4JSKw%22%7D%7D',
        'origin': 'https://www.youtube.com',
        'referer': 'https://www.youtube.com/channel/UCEgdi0XIXXZ-qJOFPf4JSKw',
        'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
        'sec-ch-ua-arch': '"x86"',
        'sec-ch-ua-bitness': '"64"',
        'sec-ch-ua-full-version': '"120.0.6099.129"',
        'sec-ch-ua-full-version-list': '"Not_A Brand";v="8.0.0.0", "Chromium";v="120.0.6099.129", "Google Chrome";v="120.0.6099.129"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-model': '""',
        'sec-ch-ua-platform': '"Windows"',
        'sec-ch-ua-platform-version': '"10.0.0"',
        'sec-ch-ua-wow64': '?0',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'same-origin',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'x-client-data': 'CKm1yQEIj7bJAQimtskBCKmdygEIhZbLAQiWocsBCJv+zAEI+ZjNAQiFoM0BCNy9zQEIj+HNAQiu6c0BCN7szQEIoe7NAQjJ7s0BCIPwzQEIhfDNARin6s0B',
        'x-goog-visitor-id': 'CgsxdVFBcm8zNDE0ZyjGmqKsBjIKCgJERRIEEgAgOg%3D%3D',
        'x-youtube-bootstrap-logged-in': 'false',
        'x-youtube-client-name': '1',
        'x-youtube-client-version': '2.20231219.04.00'
    }
    return url, payload, headers
#
#
#
#
#


def check_left_menu_catalogue_button_api():
    url = "https://www.youtube.com/youtubei/v1/browse?key=AIzaSyAO_FJ2SlqU8Q4STEHLGCilw_Y9_11qcW8&prettyPrint=false"

    payload = json.dumps({
        "context": {
            "client": {
                "hl": "ru",
                "gl": "US",
                "remoteHost": "207.244.71.81",
                "deviceMake": "",
                "deviceModel": "",
                "visitorData": "CgsxdVFBcm8zNDE0ZyjGmqKsBjIKCgJERRIEEgAgOg%3D%3D",
                "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36,gzip(gfe)",
                "clientName": "WEB",
                "clientVersion": "2.20231219.04.00",
                "osName": "Windows",
                "osVersion": "10.0",
                "originalUrl": "https://www.youtube.com/feed/guide_builder",
                "screenPixelDensity": 1,
                "platform": "DESKTOP",
                "clientFormFactor": "UNKNOWN_FORM_FACTOR",
                "configInfo": {
                    "appInstallData": "CMaaoqwGEMn3rwUQt52wBRCu1P4SEJT6_hIQ26-vBRDT4a8FEOvo_hIQmZSwBRDM364FEJqksAUQpcL-EhC36v4SEOrDrwUQ4tSuBRC--a8FEOeG_xIQ5LP-EhDcgrAFEMeDsAUQ2cmvBRCIh7AFEKaasAUQqaCwBRCZkbAFEL22rgUQ65OuBRDQjbAFEOe6rwUQooGwBRCei7AFEN3o_hIQj6KwBRCoobAFEOmMsAUQopKwBRCrgrAFEKn3rwUQmvCvBRD9n7AFEPufsAUQuIuuBRD1-a8FENfprwUQ-Z-wBRDMrv4SEJeDsAUQ1KGvBRDuoq8FEKy3rwUQzZWwBRD6krAFENWIsAUQ2piwBRCmoLAFEKSgsAUQvYqwBRC3768FEInorgUQvZmwBRCY_P4SEIjjrwUQ_IWwBRDSlbAFEKiasAUQ4fKvBRC8-a8FEKaBsAUQyPy3IhDXpLAFEOaesAUQsKWwBRDmo7AF"
                },
                "screenDensityFloat": 1.25,
                "userInterfaceTheme": "USER_INTERFACE_THEME_DARK",
                "timeZone": "Europe/Moscow",
                "browserName": "Chrome",
                "browserVersion": "120.0.0.0",
                "acceptHeader": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                "deviceExperimentId": "ChxOek14TmpJMU1qa3lOamt4T0RneE56Y3hOZz09EMaaoqwGGMaaoqwG",
                "screenWidthPoints": 1536,
                "screenHeightPoints": 260,
                "utcOffsetMinutes": 180,
                "memoryTotalKbytes": "8000000",
                "mainAppWebInfo": {
                    "graftUrl": "/feed/guide_builder",
                    "pwaInstallabilityStatus": "PWA_INSTALLABILITY_STATUS_CAN_BE_INSTALLED",
                    "webDisplayMode": "WEB_DISPLAY_MODE_BROWSER",
                    "isWebNativeShareAvailable": True
                }
            },
            "user": {
                "lockedSafetyMode": False
            },
            "request": {
                "useSsl": True,
                "internalExperimentFlags": [],
                "consistencyTokenJars": []
            },
            "clickTracking": {
                "clickTrackingParams": "CAwQtSwYACITCOOQjfHtqIMDFQYd1gAdIFML5w=="
            },
            "adSignalsInfo": {
                "params": [
                    {
                        "key": "dt",
                        "value": "1703447881561"
                    },
                    {
                        "key": "flash",
                        "value": "0"
                    },
                    {
                        "key": "frm",
                        "value": "0"
                    },
                    {
                        "key": "u_tz",
                        "value": "180"
                    },
                    {
                        "key": "u_his",
                        "value": "50"
                    },
                    {
                        "key": "u_h",
                        "value": "864"
                    },
                    {
                        "key": "u_w",
                        "value": "1536"
                    },
                    {
                        "key": "u_ah",
                        "value": "824"
                    },
                    {
                        "key": "u_aw",
                        "value": "1536"
                    },
                    {
                        "key": "u_cd",
                        "value": "24"
                    },
                    {
                        "key": "bc",
                        "value": "31"
                    },
                    {
                        "key": "bih",
                        "value": "260"
                    },
                    {
                        "key": "biw",
                        "value": "1519"
                    },
                    {
                        "key": "brdim",
                        "value": "0,0,0,0,1536,0,1536,824,1536,260"
                    },
                    {
                        "key": "vis",
                        "value": "1"
                    },
                    {
                        "key": "wgl",
                        "value": "true"
                    },
                    {
                        "key": "ca_type",
                        "value": "image"
                    }
                ]
            }
        },
        "browseId": "FEguide_builder"
    })
    headers = {
        'authority': 'www.youtube.com',
        'accept': '*/*',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/json',
        'cookie': 'CONSENT=PENDING+917; SOCS=CAISEwgDEgk1ODE3OTQxMTEaAnJ1IAEaBgiAlNCqBg; wide=1; _gcl_au=1.1.1236695019.1702128731; _ga=GA1.1.46170218.1702128973; PREF=f4=4000000&f6=40000000&tz=Europe.Moscow&f7=100&f5=30000&guide_collapsed=true; _ga_VCGEPY40VB=GS1.1.1702217844.6.0.1702217844.0.0.0; VISITOR_PRIVACY_METADATA=CgJERRIEEgAgOg%3D%3D; VISITOR_INFO1_LIVE=1uQAro3414g; YSC=mbg-Ztr7WdQ; GPS=1; ST-12bolcm=itct=CAwQtSwYACITCOOQjfHtqIMDFQYd1gAdIFML5w%3D%3D&csn=MC4wMzA2NDgyNjk2NTU5Njg4OTY.&endpoint=%7B%22clickTrackingParams%22%3A%22CAwQtSwYACITCOOQjfHtqIMDFQYd1gAdIFML5w%3D%3D%22%2C%22commandMetadata%22%3A%7B%22webCommandMetadata%22%3A%7B%22url%22%3A%22%2Ffeed%2Fguide_builder%22%2C%22webPageType%22%3A%22WEB_PAGE_TYPE_BROWSE%22%2C%22rootVe%22%3A6827%2C%22apiUrl%22%3A%22%2Fyoutubei%2Fv1%2Fbrowse%22%7D%7D%2C%22browseEndpoint%22%3A%7B%22browseId%22%3A%22FEguide_builder%22%7D%7D',
        'origin': 'https://www.youtube.com',
        'referer': 'https://www.youtube.com/feed/guide_builder',
        'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
        'sec-ch-ua-arch': '"x86"',
        'sec-ch-ua-bitness': '"64"',
        'sec-ch-ua-full-version': '"120.0.6099.129"',
        'sec-ch-ua-full-version-list': '"Not_A Brand";v="8.0.0.0", "Chromium";v="120.0.6099.129", "Google Chrome";v="120.0.6099.129"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-model': '""',
        'sec-ch-ua-platform': '"Windows"',
        'sec-ch-ua-platform-version': '"10.0.0"',
        'sec-ch-ua-wow64': '?0',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'same-origin',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'x-client-data': 'CKm1yQEIj7bJAQimtskBCKmdygEIhZbLAQiWocsBCJv+zAEI+ZjNAQiFoM0BCNy9zQEIj+HNAQiu6c0BCN7szQEIoe7NAQjJ7s0BCIPwzQEIhfDNARin6s0B',
        'x-goog-visitor-id': 'CgsxdVFBcm8zNDE0ZyjGmqKsBjIKCgJERRIEEgAgOg%3D%3D',
        'x-youtube-bootstrap-logged-in': 'false',
        'x-youtube-client-name': '1',
        'x-youtube-client-version': '2.20231219.04.00'
    }
    return url, payload, headers
#
#
#
#
#


def check_left_menu_premium_button_api():
    url = "https://www.youtube.com/youtubei/v1/browse?key=AIzaSyAO_FJ2SlqU8Q4STEHLGCilw_Y9_11qcW8&prettyPrint=false"

    payload = json.dumps({
        "context": {
            "client": {
                "hl": "ru",
                "gl": "US",
                "remoteHost": "207.244.71.81",
                "deviceMake": "",
                "deviceModel": "",
                "visitorData": "CgsxdVFBcm8zNDE0ZyjGmqKsBjIKCgJERRIEEgAgOg%3D%3D",
                "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36,gzip(gfe)",
                "clientName": "WEB",
                "clientVersion": "2.20231219.04.00",
                "osName": "Windows",
                "osVersion": "10.0",
                "originalUrl": "https://www.youtube.com/premium",
                "screenPixelDensity": 1,
                "platform": "DESKTOP",
                "clientFormFactor": "UNKNOWN_FORM_FACTOR",
                "configInfo": {
                    "appInstallData": "CMaaoqwGEMn3rwUQt52wBRCu1P4SEJT6_hIQ26-vBRDT4a8FEOvo_hIQmZSwBRDM364FEJqksAUQpcL-EhC36v4SEOrDrwUQ4tSuBRC--a8FEOeG_xIQ5LP-EhDcgrAFEMeDsAUQ2cmvBRCIh7AFEKaasAUQqaCwBRCZkbAFEL22rgUQ65OuBRDQjbAFEOe6rwUQooGwBRCei7AFEN3o_hIQj6KwBRCoobAFEOmMsAUQopKwBRCrgrAFEKn3rwUQmvCvBRD9n7AFEPufsAUQuIuuBRD1-a8FENfprwUQ-Z-wBRDMrv4SEJeDsAUQ1KGvBRDuoq8FEKy3rwUQzZWwBRD6krAFENWIsAUQ2piwBRCmoLAFEKSgsAUQvYqwBRC3768FEInorgUQvZmwBRCY_P4SEIjjrwUQ_IWwBRDSlbAFEKiasAUQ4fKvBRC8-a8FEKaBsAUQyPy3IhDXpLAFEOaesAUQsKWwBRDmo7AF"
                },
                "screenDensityFloat": 1.25,
                "userInterfaceTheme": "USER_INTERFACE_THEME_DARK",
                "timeZone": "Europe/Moscow",
                "browserName": "Chrome",
                "browserVersion": "120.0.0.0",
                "acceptHeader": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                "deviceExperimentId": "ChxOek14TmpJMU1qa3lOamt4T0RneE56Y3hOZz09EMaaoqwGGMaaoqwG",
                "screenWidthPoints": 1536,
                "screenHeightPoints": 260,
                "utcOffsetMinutes": 180,
                "memoryTotalKbytes": "8000000",
                "mainAppWebInfo": {
                    "graftUrl": "/premium",
                    "pwaInstallabilityStatus": "PWA_INSTALLABILITY_STATUS_CAN_BE_INSTALLED",
                    "webDisplayMode": "WEB_DISPLAY_MODE_BROWSER",
                    "isWebNativeShareAvailable": True
                }
            },
            "user": {
                "lockedSafetyMode": False
            },
            "request": {
                "useSsl": True,
                "internalExperimentFlags": [],
                "consistencyTokenJars": []
            },
            "clickTracking": {
                "clickTrackingParams": "CAoQmbcBGAAiEwjjkI3x7aiDAxUGHdYAHSBTC-c="
            },
            "adSignalsInfo": {
                "params": [
                    {
                        "key": "dt",
                        "value": "1703447881561"
                    },
                    {
                        "key": "flash",
                        "value": "0"
                    },
                    {
                        "key": "frm",
                        "value": "0"
                    },
                    {
                        "key": "u_tz",
                        "value": "180"
                    },
                    {
                        "key": "u_his",
                        "value": "50"
                    },
                    {
                        "key": "u_h",
                        "value": "864"
                    },
                    {
                        "key": "u_w",
                        "value": "1536"
                    },
                    {
                        "key": "u_ah",
                        "value": "824"
                    },
                    {
                        "key": "u_aw",
                        "value": "1536"
                    },
                    {
                        "key": "u_cd",
                        "value": "24"
                    },
                    {
                        "key": "bc",
                        "value": "31"
                    },
                    {
                        "key": "bih",
                        "value": "260"
                    },
                    {
                        "key": "biw",
                        "value": "1519"
                    },
                    {
                        "key": "brdim",
                        "value": "0,0,0,0,1536,0,1536,824,1536,260"
                    },
                    {
                        "key": "vis",
                        "value": "1"
                    },
                    {
                        "key": "wgl",
                        "value": "true"
                    },
                    {
                        "key": "ca_type",
                        "value": "image"
                    }
                ]
            }
        },
        "browseId": "SPunlimited"
    })
    headers = {
        'authority': 'www.youtube.com',
        'accept': '*/*',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/json',
        'cookie': 'CONSENT=PENDING+917; SOCS=CAISEwgDEgk1ODE3OTQxMTEaAnJ1IAEaBgiAlNCqBg; wide=1; _gcl_au=1.1.1236695019.1702128731; _ga=GA1.1.46170218.1702128973; PREF=f4=4000000&f6=40000000&tz=Europe.Moscow&f7=100&f5=30000&guide_collapsed=true; _ga_VCGEPY40VB=GS1.1.1702217844.6.0.1702217844.0.0.0; VISITOR_PRIVACY_METADATA=CgJERRIEEgAgOg%3D%3D; VISITOR_INFO1_LIVE=1uQAro3414g; YSC=mbg-Ztr7WdQ; ST-1yupr2g=itct=CAoQmbcBGAAiEwjjkI3x7aiDAxUGHdYAHSBTC-c%3D&csn=MC41MDAzOTQ3ODg3Njc5Mjg1&endpoint=%7B%22clickTrackingParams%22%3A%22CAoQmbcBGAAiEwjjkI3x7aiDAxUGHdYAHSBTC-c%3D%22%2C%22commandMetadata%22%3A%7B%22webCommandMetadata%22%3A%7B%22url%22%3A%22%2Fpremium%22%2C%22webPageType%22%3A%22WEB_PAGE_TYPE_BROWSE%22%2C%22rootVe%22%3A11487%2C%22apiUrl%22%3A%22%2Fyoutubei%2Fv1%2Fbrowse%22%7D%7D%2C%22browseEndpoint%22%3A%7B%22browseId%22%3A%22SPunlimited%22%7D%7D',
        'origin': 'https://www.youtube.com',
        'referer': 'https://www.youtube.com/premium',
        'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
        'sec-ch-ua-arch': '"x86"',
        'sec-ch-ua-bitness': '"64"',
        'sec-ch-ua-full-version': '"120.0.6099.129"',
        'sec-ch-ua-full-version-list': '"Not_A Brand";v="8.0.0.0", "Chromium";v="120.0.6099.129", "Google Chrome";v="120.0.6099.129"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-model': '""',
        'sec-ch-ua-platform': '"Windows"',
        'sec-ch-ua-platform-version': '"10.0.0"',
        'sec-ch-ua-wow64': '?0',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'same-origin',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'x-client-data': 'CKm1yQEIj7bJAQimtskBCKmdygEIhZbLAQiWocsBCJv+zAEI+ZjNAQiFoM0BCNy9zQEIj+HNAQiu6c0BCN7szQEIoe7NAQjJ7s0BCIPwzQEIhfDNARin6s0B',
        'x-goog-visitor-id': 'CgsxdVFBcm8zNDE0ZyjGmqKsBjIKCgJERRIEEgAgOg%3D%3D',
        'x-youtube-bootstrap-logged-in': 'false',
        'x-youtube-client-name': '1',
        'x-youtube-client-version': '2.20231219.04.00'
    }
    return url, payload, headers
#
#
#
#
#


def check_left_menu_yt_music_button_api():
    url = "https://music.youtube.com/youtubei/v1/account/account_menu?key=AIzaSyC9XL3ZjWddXya6X74dJoCTL-WEYFDNX30&prettyPrint=false"

    payload = json.dumps({
        "context": {
            "client": {
                "hl": "ru",
                "gl": "US",
                "remoteHost": "162.210.194.38",
                "deviceMake": "",
                "deviceModel": "",
                "visitorData": "CgsxdVFBcm8zNDE0ZyjahaasBjIKCgJERRIEEgAgOg%3D%3D",
                "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36,gzip(gfe)",
                "clientName": "WEB_REMIX",
                "clientVersion": "1.20231214.00.00",
                "osName": "Windows",
                "osVersion": "10.0",
                "originalUrl": "https://music.youtube.com/",
                "screenPixelDensity": 1,
                "platform": "DESKTOP",
                "clientFormFactor": "UNKNOWN_FORM_FACTOR",
                "configInfo": {
                    "appInstallData": "CNqFpqwGEIiHsAUQ65OuBRCY_P4SELfvrwUQ-5-wBRC9irAFENCNsAUQuIuuBRCpoLAFEOSz_hIQq4KwBRD9n7AFEL22rgUQ1YiwBRD9uP0SEOmMsAUQ3ej-EhDnuq8FEKihsAUQyfevBRDSlbAFEJmUsAUQrtT-EhCmgbAFEJqksAUQ2piwBRDqw68FEKSgsAUQj6KwBRCmoLAFEM2VsAUQ2cmvBRDh8q8FEPX5rwUQrLevBRComrAFENPhrwUQ54b_EhD8hbAFEKKBsAUQzN-uBRCa8K8FELfq_hIQx4OwBRCI468FEL75rwUQvZmwBRCei7AFELedsAUQpcL-EhCU-v4SEMyu_hIQqfevBRCikrAFELz5rwUQ6-j-EhD5n7AFENeksAU%3D",
                    "coldConfigData": None,
                    "coldHashData": None,
                    "hotHashData": None
                },
                "screenDensityFloat": 1.25,
                "userInterfaceTheme": "USER_INTERFACE_THEME_DARK",
                "timeZone": "Europe/Moscow",
                "browserName": "Chrome",
                "browserVersion": "120.0.0.0",
                "acceptHeader": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                "deviceExperimentId": "ChxOek14TmpVeU1qazBNekV4TURjNE9EZzFNUT09ENqFpqwGGNqFpqwG",
                "screenWidthPoints": 1536,
                "screenHeightPoints": 260,
                "utcOffsetMinutes": 180,
                "musicAppInfo": {
                    "webDisplayMode": "WEB_DISPLAY_MODE_BROWSER",
                    "storeDigitalGoodsApiSupportStatus": {
                        "playStoreDigitalGoodsApiSupportStatus": "DIGITAL_GOODS_API_SUPPORT_STATUS_UNSUPPORTED"
                    }
                }
            },
            "user": {
                "lockedSafetyMode": False
            },
            "request": {
                "useSsl": True,
                "internalExperimentFlags": [],
                "consistencyTokenJars": []
            },
            "adSignalsInfo": {
                "params": [
                    {
                        "key": "dt",
                        "value": "1703510748660"
                    },
                    {
                        "key": "flash",
                        "value": "0"
                    },
                    {
                        "key": "frm",
                        "value": "0"
                    },
                    {
                        "key": "u_tz",
                        "value": "180"
                    },
                    {
                        "key": "u_his",
                        "value": "1"
                    },
                    {
                        "key": "u_h",
                        "value": "864"
                    },
                    {
                        "key": "u_w",
                        "value": "1536"
                    },
                    {
                        "key": "u_ah",
                        "value": "824"
                    },
                    {
                        "key": "u_aw",
                        "value": "1536"
                    },
                    {
                        "key": "u_cd",
                        "value": "24"
                    },
                    {
                        "key": "bc",
                        "value": "31"
                    },
                    {
                        "key": "bih",
                        "value": "260"
                    },
                    {
                        "key": "biw",
                        "value": "1536"
                    },
                    {
                        "key": "brdim",
                        "value": "0,0,0,0,1536,0,1536,824,1536,260"
                    },
                    {
                        "key": "vis",
                        "value": "1"
                    },
                    {
                        "key": "wgl",
                        "value": "true"
                    },
                    {
                        "key": "ca_type",
                        "value": "image"
                    }
                ]
            }
        },
        "userInterfaceTheme": "USER_INTERFACE_THEME_DARK",
        "deviceTheme": "DEVICE_THEME_SELECTED"
    })
    headers = {
        'authority': 'music.youtube.com',
        'accept': '*/*',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/json',
        'cookie': 'CONSENT=PENDING+917; SOCS=CAISEwgDEgk1ODE3OTQxMTEaAnJ1IAEaBgiAlNCqBg; wide=1; _gcl_au=1.1.1236695019.1702128731; _ga=GA1.1.46170218.1702128973; PREF=f4=4000000&f6=40000000&tz=Europe.Moscow&f7=100&f5=30000&guide_collapsed=true; VISITOR_PRIVACY_METADATA=CgJERRIEEgAgOg%3D%3D; VISITOR_INFO1_LIVE=1uQAro3414g; YSC=mbg-Ztr7WdQ; _ga_VCGEPY40VB=GS1.1.1703510732.9.0.1703510732.0.0.0; GPS=1',
        'origin': 'https://music.youtube.com',
        'referer': 'https://music.youtube.com/',
        'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
        'sec-ch-ua-arch': '"x86"',
        'sec-ch-ua-bitness': '"64"',
        'sec-ch-ua-full-version': '"120.0.6099.129"',
        'sec-ch-ua-full-version-list': '"Not_A Brand";v="8.0.0.0", "Chromium";v="120.0.6099.129", "Google Chrome";v="120.0.6099.129"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-model': '""',
        'sec-ch-ua-platform': '"Windows"',
        'sec-ch-ua-platform-version': '"10.0.0"',
        'sec-ch-ua-wow64': '?0',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'same-origin',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'x-client-data': 'CKm1yQEIj7bJAQimtskBCKmdygEIhZbLAQiVocsBCJv+zAEI+ZjNAQiFoM0BCNy9zQEIj+HNAQiu6c0BCN7szQEIoe7NAQjJ7s0BCIPwzQEIhfDNARin6s0B',
        'x-goog-visitor-id': 'CgsxdVFBcm8zNDE0ZyjahaasBjIKCgJERRIEEgAgOg%3D%3D',
        'x-youtube-bootstrap-logged-in': 'false',
        'x-youtube-client-name': '67',
        'x-youtube-client-version': '1.20231214.00.00'
    }
    return url, payload, headers
#
#
#
#
#


def check_left_menu_yt_kids_button_api():
    url = "https://www.youtubekids.com/youtubei/v1/kids/get_kids_flow_data?alt=json&key=AIzaSyBbZV_fZ3an51sF-mvs5w37OqqbsTOzwtU"

    payload = json.dumps({
        "context": {
            "client": {
                "clientName": "WEB_KIDS",
                "clientVersion": "2.20231212.08.00",
                "hl": "ru",
                "gl": "US",
                "experimentIds": [],
                "experimentsToken": "",
                "browserName": "Chrome",
                "browserVersion": "120.0.0.0",
                "osName": "Windows",
                "osVersion": "10.0",
                "platform": "DESKTOP"
            },
            "capabilities": {},
            "request": {
                "internalExperimentFlags": []
            }
        },
        "flowTypes": [
            "KIDS_FLOW_TYPE_ONBOARDING"
        ]
    })
    headers = {
        'authority': 'www.youtubekids.com',
        'accept': '*/*',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/json',
        'cookie': 'YSC=-rKXlFUbEKU; DEVICE_INFO=ChxOek14TURVNE56TXlOVE01TkRVME1UUXhOUT09EPDY0asGGPDY0asG',
        'origin': 'https://www.youtubekids.com',
        'referer': 'https://www.youtubekids.com/?source=youtube_web',
        'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
        'sec-ch-ua-arch': '"x86"',
        'sec-ch-ua-bitness': '"64"',
        'sec-ch-ua-full-version': '"120.0.6099.129"',
        'sec-ch-ua-full-version-list': '"Not_A Brand";v="8.0.0.0", "Chromium";v="120.0.6099.129", "Google Chrome";v="120.0.6099.129"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-model': '""',
        'sec-ch-ua-platform': '"Windows"',
        'sec-ch-ua-platform-version': '"10.0.0"',
        'sec-ch-ua-wow64': '?0',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'x-client-data': 'CKm1yQEIj7bJAQimtskBCKmdygEIhZbLAQiVocsBCJv+zAEI+ZjNAQiFoM0BCNy9zQEIj+HNAQiu6c0BCN7szQEIoe7NAQjJ7s0BCIPwzQEIhfDNARin6s0B',
        'x-goog-visitor-id': 'Cgs2NDktLVJzTms1Zyi48darBjIKCgJCWRIEGgAgZA%3D%3D',
        'x-youtube-ad-signals': 'dt=1703511802302&flash=0&frm&u_tz=180&u_his=1&u_h=864&u_w=1536&u_ah=824&u_aw=1536&u_cd=24&bc=31&bih=260&biw=1536&brdim=0%2C0%2C0%2C0%2C1536%2C0%2C1536%2C824%2C1536%2C260&vis=1&wgl=true&ca_type=image',
        'x-youtube-client-name': '76',
        'x-youtube-client-version': '2.20231212.08.00',
        'x-youtube-device': 'cbr=Chrome&cbrver=120.0.0.0&ceng=WebKit&cengver=537.36&cos=Windows&cosver=10.0&cplatform=DESKTOP',
        'x-youtube-page-cl': '590345707',
        'x-youtube-page-label': 'youtube.kids.web.polymer.scs_20231212_08_RC00',
        'x-youtube-time-zone': 'Europe/Moscow',
        'x-youtube-utc-offset': '180'
    }
    return url, payload, headers
#
#
#
#
#


def check_left_menu_reports_button_api():
    url = "https://www.youtube.com/youtubei/v1/browse?key=AIzaSyAO_FJ2SlqU8Q4STEHLGCilw_Y9_11qcW8&prettyPrint=false"

    payload = json.dumps({
        "context": {
            "client": {
                "hl": "ru",
                "gl": "US",
                "remoteHost": "162.210.194.38",
                "deviceMake": "",
                "deviceModel": "",
                "visitorData": "CgsxdVFBcm8zNDE0ZyiRk6asBjIKCgJERRIEEgAgOg%3D%3D",
                "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36,gzip(gfe)",
                "clientName": "WEB",
                "clientVersion": "2.20231219.04.00",
                "osName": "Windows",
                "osVersion": "10.0",
                "originalUrl": "https://www.youtube.com/reporthistory",
                "screenPixelDensity": 1,
                "platform": "DESKTOP",
                "clientFormFactor": "UNKNOWN_FORM_FACTOR",
                "configInfo": {
                    "appInstallData": "CJGTpqwGELfq_hIQrtT-EhDcgrAFENShrwUQooGwBRDi1K4FEL22rgUQ6YywBRDZya8FEOe6rwUQvvmvBRDh8q8FENfprwUQ6sOvBRD5n7AFEKmgsAUQ54b_EhD6krAFENPhrwUQq4KwBRC8-a8FEPufsAUQ2piwBRCU-v4SEOuTrgUQzN-uBRCa8K8FEM2VsAUQzK7-EhCoobAFEPX5rwUQiOOvBRDr6P4SEKiasAUQiIewBRC9mbAFEJj8_hIQpcL-EhC9irAFEKaasAUQl4OwBRDbr68FEKy3rwUQ1YiwBRDSlbAFEO6irwUQ3ej-EhCZkbAFEJqksAUQnouwBRC3768FEPyFsAUQt52wBRCmoLAFEI-isAUQopKwBRCJ6K4FENCNsAUQ5LP-EhDJ968FEMeDsAUQuIuuBRCp968FEJmUsAUQpKCwBRD9n7AFEKaBsAUQ16SwBRCwpbAFEOaesAUQ5qOwBQ%3D%3D"
                },
                "screenDensityFloat": 1.25,
                "userInterfaceTheme": "USER_INTERFACE_THEME_DARK",
                "timeZone": "Europe/Moscow",
                "browserName": "Chrome",
                "browserVersion": "120.0.0.0",
                "acceptHeader": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                "deviceExperimentId": "ChxOek14TmpVek1ETXlOams1TmpZM05EWTJPUT09EJGTpqwGGJGTpqwG",
                "screenWidthPoints": 1536,
                "screenHeightPoints": 260,
                "utcOffsetMinutes": 180,
                "memoryTotalKbytes": "8000000",
                "mainAppWebInfo": {
                    "graftUrl": "/reporthistory",
                    "pwaInstallabilityStatus": "PWA_INSTALLABILITY_STATUS_CAN_BE_INSTALLED",
                    "webDisplayMode": "WEB_DISPLAY_MODE_BROWSER",
                    "isWebNativeShareAvailable": True
                }
            },
            "user": {
                "lockedSafetyMode": False
            },
            "request": {
                "useSsl": True,
                "internalExperimentFlags": [],
                "consistencyTokenJars": []
            },
            "clickTracking": {
                "clickTrackingParams": "CAQQtSwYASITCKKI5rveqoMDFeEE1gAdER8JUw=="
            },
            "adSignalsInfo": {
                "params": [
                    {
                        "key": "dt",
                        "value": "1703512467120"
                    },
                    {
                        "key": "flash",
                        "value": "0"
                    },
                    {
                        "key": "frm",
                        "value": "0"
                    },
                    {
                        "key": "u_tz",
                        "value": "180"
                    },
                    {
                        "key": "u_his",
                        "value": "11"
                    },
                    {
                        "key": "u_h",
                        "value": "864"
                    },
                    {
                        "key": "u_w",
                        "value": "1536"
                    },
                    {
                        "key": "u_ah",
                        "value": "824"
                    },
                    {
                        "key": "u_aw",
                        "value": "1536"
                    },
                    {
                        "key": "u_cd",
                        "value": "24"
                    },
                    {
                        "key": "bc",
                        "value": "31"
                    },
                    {
                        "key": "bih",
                        "value": "260"
                    },
                    {
                        "key": "biw",
                        "value": "1520"
                    },
                    {
                        "key": "brdim",
                        "value": "0,0,0,0,1536,0,1536,824,1536,260"
                    },
                    {
                        "key": "vis",
                        "value": "1"
                    },
                    {
                        "key": "wgl",
                        "value": "true"
                    },
                    {
                        "key": "ca_type",
                        "value": "image"
                    }
                ]
            }
        },
        "browseId": "SPreport_history"
    })
    headers = {
        'authority': 'www.youtube.com',
        'accept': '*/*',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/json',
        'cookie': 'CONSENT=PENDING+917; SOCS=CAISEwgDEgk1ODE3OTQxMTEaAnJ1IAEaBgiAlNCqBg; wide=1; _gcl_au=1.1.1236695019.1702128731; _ga=GA1.1.46170218.1702128973; VISITOR_PRIVACY_METADATA=CgJERRIEEgAgOg%3D%3D; VISITOR_INFO1_LIVE=1uQAro3414g; YSC=mbg-Ztr7WdQ; _ga_VCGEPY40VB=GS1.1.1703510732.9.1.1703512434.0.0.0; PREF=f4=4000000&f6=40000000&tz=Europe.Moscow&f7=100&f5=30000&guide_collapsed=true; GPS=1; ST-6btxch=itct=CAQQtSwYASITCKKI5rveqoMDFeEE1gAdER8JUw%3D%3D&csn=MC4xMDcyNDk5NzM1MjI0Mjg2&endpoint=%7B%22clickTrackingParams%22%3A%22CAQQtSwYASITCKKI5rveqoMDFeEE1gAdER8JUw%3D%3D%22%2C%22commandMetadata%22%3A%7B%22webCommandMetadata%22%3A%7B%22url%22%3A%22%2Freporthistory%22%2C%22webPageType%22%3A%22WEB_PAGE_TYPE_BROWSE%22%2C%22rootVe%22%3A6827%2C%22apiUrl%22%3A%22%2Fyoutubei%2Fv1%2Fbrowse%22%7D%7D%2C%22browseEndpoint%22%3A%7B%22browseId%22%3A%22SPreport_history%22%7D%7D',
        'origin': 'https://www.youtube.com',
        'referer': 'https://www.youtube.com/reporthistory',
        'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
        'sec-ch-ua-arch': '"x86"',
        'sec-ch-ua-bitness': '"64"',
        'sec-ch-ua-full-version': '"120.0.6099.129"',
        'sec-ch-ua-full-version-list': '"Not_A Brand";v="8.0.0.0", "Chromium";v="120.0.6099.129", "Google Chrome";v="120.0.6099.129"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-model': '""',
        'sec-ch-ua-platform': '"Windows"',
        'sec-ch-ua-platform-version': '"10.0.0"',
        'sec-ch-ua-wow64': '?0',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'same-origin',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'x-client-data': 'CKm1yQEIj7bJAQimtskBCKmdygEIhZbLAQiVocsBCJv+zAEI+ZjNAQiFoM0BCNy9zQEIj+HNAQiu6c0BCN7szQEIoe7NAQjJ7s0BCIPwzQEIhfDNARin6s0B',
        'x-goog-visitor-id': 'CgsxdVFBcm8zNDE0ZyiRk6asBjIKCgJERRIEEgAgOg%3D%3D',
        'x-youtube-bootstrap-logged-in': 'false',
        'x-youtube-client-name': '1',
        'x-youtube-client-version': '2.20231219.04.00'
    }
    return url, payload, headers
#
#
#
#
#


def check_closed_left_menu_main_button_api():
    url = "https://www.youtube.com/youtubei/v1/browse?key=AIzaSyAO_FJ2SlqU8Q4STEHLGCilw_Y9_11qcW8&prettyPrint=false"

    payload = json.dumps({
        "context": {
            "client": {
                "hl": "ru",
                "gl": "US",
                "remoteHost": "162.210.194.38",
                "deviceMake": "",
                "deviceModel": "",
                "visitorData": "CgsxdVFBcm8zNDE0ZyiHmKasBjIKCgJERRIEEgAgOg%3D%3D",
                "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36,gzip(gfe)",
                "clientName": "WEB",
                "clientVersion": "2.20231219.04.00",
                "osName": "Windows",
                "osVersion": "10.0",
                "originalUrl": "https://www.youtube.com/",
                "screenPixelDensity": 1,
                "platform": "DESKTOP",
                "clientFormFactor": "UNKNOWN_FORM_FACTOR",
                "configInfo": {
                    "appInstallData": "CIeYpqwGEJmUsAUQiIewBRCu1P4SEJT6_hIQ65OuBRC8-a8FEJqksAUQ1YiwBRC3768FENfprwUQyfevBRDnhv8SEM2VsAUQ_Z-wBRC9tq4FENShrwUQieiuBRCZkbAFEPufsAUQvvmvBRDnuq8FENPhrwUQ_IWwBRCmmrAFEOmMsAUQ3IKwBRC9mbAFEKSgsAUQ9fmvBRComrAFEKKBsAUQnouwBRCikrAFEJj8_hIQmvCvBRCst68FEJeDsAUQiOOvBRDd6P4SENqYsAUQ5LP-EhDQjbAFEKagsAUQj6KwBRD6krAFEKuCsAUQ4tSuBRDSlbAFEMzfrgUQzK7-EhDbr68FEOHyrwUQ7qKvBRDHg7AFEPmfsAUQqfevBRC9irAFEKmgsAUQ6-j-EhDZya8FELfq_hIQt52wBRC4i64FEOrDrwUQpcL-EhCoobAFEKaBsAUQ16SwBRDmnrAFEOajsAUQsKWwBQ%3D%3D"
                },
                "screenDensityFloat": 1.25,
                "userInterfaceTheme": "USER_INTERFACE_THEME_DARK",
                "timeZone": "Europe/Moscow",
                "browserName": "Chrome",
                "browserVersion": "120.0.0.0",
                "acceptHeader": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                "deviceExperimentId": "ChxOek14TmpVek16QXpNekE1TlRFNE9ETTVNdz09EIeYpqwGGIeYpqwG",
                "screenWidthPoints": 1536,
                "screenHeightPoints": 338,
                "utcOffsetMinutes": 180,
                "memoryTotalKbytes": "8000000",
                "mainAppWebInfo": {
                    "graftUrl": "/",
                    "pwaInstallabilityStatus": "PWA_INSTALLABILITY_STATUS_CAN_BE_INSTALLED",
                    "webDisplayMode": "WEB_DISPLAY_MODE_BROWSER",
                    "isWebNativeShareAvailable": True
                }
            },
            "user": {
                "lockedSafetyMode": False
            },
            "request": {
                "useSsl": True,
                "internalExperimentFlags": [],
                "consistencyTokenJars": []
            },
            "clickTracking": {
                "clickTrackingParams": "CB8Q8KgHGAAiEwiLxa3o4KqDAxWFGtYAHUoYBog="
            },
            "adSignalsInfo": {
                "params": [
                    {
                        "key": "dt",
                        "value": "1703513096807"
                    },
                    {
                        "key": "flash",
                        "value": "0"
                    },
                    {
                        "key": "frm",
                        "value": "0"
                    },
                    {
                        "key": "u_tz",
                        "value": "180"
                    },
                    {
                        "key": "u_his",
                        "value": "17"
                    },
                    {
                        "key": "u_h",
                        "value": "864"
                    },
                    {
                        "key": "u_w",
                        "value": "1536"
                    },
                    {
                        "key": "u_ah",
                        "value": "824"
                    },
                    {
                        "key": "u_aw",
                        "value": "1536"
                    },
                    {
                        "key": "u_cd",
                        "value": "24"
                    },
                    {
                        "key": "bc",
                        "value": "31"
                    },
                    {
                        "key": "bih",
                        "value": "338"
                    },
                    {
                        "key": "biw",
                        "value": "1520"
                    },
                    {
                        "key": "brdim",
                        "value": "0,0,0,0,1536,0,1536,824,1536,338"
                    },
                    {
                        "key": "vis",
                        "value": "1"
                    },
                    {
                        "key": "wgl",
                        "value": "true"
                    },
                    {
                        "key": "ca_type",
                        "value": "image"
                    }
                ]
            }
        },
        "browseId": "FEwhat_to_watch",
        "inlineSettingStatus": "INLINE_SETTING_STATUS_ON"
    })
    headers = {
        'authority': 'www.youtube.com',
        'accept': '*/*',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/json',
        'cookie': 'CONSENT=PENDING+917; SOCS=CAISEwgDEgk1ODE3OTQxMTEaAnJ1IAEaBgiAlNCqBg; wide=1; _gcl_au=1.1.1236695019.1702128731; _ga=GA1.1.46170218.1702128973; VISITOR_PRIVACY_METADATA=CgJERRIEEgAgOg%3D%3D; VISITOR_INFO1_LIVE=1uQAro3414g; YSC=mbg-Ztr7WdQ; _ga_VCGEPY40VB=GS1.1.1703510732.9.1.1703512434.0.0.0; GPS=1; PREF=f4=4010000&f6=40000000&tz=Europe.Moscow&f7=100&f5=30000&guide_collapsed=true; ST-1b=itct=CB8Q8KgHGAAiEwiLxa3o4KqDAxWFGtYAHUoYBog%3D&csn=MC45NjQ1NTA2MzAxMjE5NDMz&endpoint=%7B%22clickTrackingParams%22%3A%22CB8Q8KgHGAAiEwiLxa3o4KqDAxWFGtYAHUoYBog%3D%22%2C%22commandMetadata%22%3A%7B%22webCommandMetadata%22%3A%7B%22url%22%3A%22%2F%22%2C%22webPageType%22%3A%22WEB_PAGE_TYPE_BROWSE%22%2C%22rootVe%22%3A3854%2C%22apiUrl%22%3A%22%2Fyoutubei%2Fv1%2Fbrowse%22%7D%7D%2C%22browseEndpoint%22%3A%7B%22browseId%22%3A%22FEwhat_to_watch%22%7D%7D',
        'origin': 'https://www.youtube.com',
        'referer': 'https://www.youtube.com/',
        'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
        'sec-ch-ua-arch': '"x86"',
        'sec-ch-ua-bitness': '"64"',
        'sec-ch-ua-full-version': '"120.0.6099.129"',
        'sec-ch-ua-full-version-list': '"Not_A Brand";v="8.0.0.0", "Chromium";v="120.0.6099.129", "Google Chrome";v="120.0.6099.129"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-model': '""',
        'sec-ch-ua-platform': '"Windows"',
        'sec-ch-ua-platform-version': '"10.0.0"',
        'sec-ch-ua-wow64': '?0',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'same-origin',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'x-client-data': 'CKm1yQEIj7bJAQimtskBCKmdygEIhZbLAQiVocsBCJv+zAEI+ZjNAQiFoM0BCNy9zQEIj+HNAQiu6c0BCN7szQEIoe7NAQjJ7s0BCIPwzQEIhfDNARin6s0B',
        'x-goog-visitor-id': 'CgsxdVFBcm8zNDE0ZyiHmKasBjIKCgJERRIEEgAgOg%3D%3D',
        'x-youtube-bootstrap-logged-in': 'false',
        'x-youtube-client-name': '1',
        'x-youtube-client-version': '2.20231219.04.00'
    }
    return url, payload, headers
#
#
#
#
#


def check_closed_left_menu_subscriptions_button_api():
    url = "https://www.youtube.com/youtubei/v1/browse?key=AIzaSyAO_FJ2SlqU8Q4STEHLGCilw_Y9_11qcW8&prettyPrint=false"

    payload = json.dumps({
        "context": {
            "client": {
                "hl": "ru",
                "gl": "US",
                "remoteHost": "162.210.194.38",
                "deviceMake": "",
                "deviceModel": "",
                "visitorData": "CgsxdVFBcm8zNDE0ZyiHmKasBjIKCgJERRIEEgAgOg%3D%3D",
                "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36,gzip(gfe)",
                "clientName": "WEB",
                "clientVersion": "2.20231219.04.00",
                "osName": "Windows",
                "osVersion": "10.0",
                "originalUrl": "https://www.youtube.com/feed/subscriptions",
                "screenPixelDensity": 1,
                "platform": "DESKTOP",
                "clientFormFactor": "UNKNOWN_FORM_FACTOR",
                "configInfo": {
                    "appInstallData": "CIeYpqwGEJmUsAUQiIewBRCu1P4SEJT6_hIQ65OuBRC8-a8FEJqksAUQ1YiwBRC3768FENfprwUQyfevBRDnhv8SEM2VsAUQ_Z-wBRC9tq4FENShrwUQieiuBRCZkbAFEPufsAUQvvmvBRDnuq8FENPhrwUQ_IWwBRCmmrAFEOmMsAUQ3IKwBRC9mbAFEKSgsAUQ9fmvBRComrAFEKKBsAUQnouwBRCikrAFEJj8_hIQmvCvBRCst68FEJeDsAUQiOOvBRDd6P4SENqYsAUQ5LP-EhDQjbAFEKagsAUQj6KwBRD6krAFEKuCsAUQ4tSuBRDSlbAFEMzfrgUQzK7-EhDbr68FEOHyrwUQ7qKvBRDHg7AFEPmfsAUQqfevBRC9irAFEKmgsAUQ6-j-EhDZya8FELfq_hIQt52wBRC4i64FEOrDrwUQpcL-EhCoobAFEKaBsAUQ16SwBRDmnrAFEOajsAUQsKWwBQ%3D%3D"
                },
                "screenDensityFloat": 1.25,
                "userInterfaceTheme": "USER_INTERFACE_THEME_DARK",
                "timeZone": "Europe/Moscow",
                "browserName": "Chrome",
                "browserVersion": "120.0.0.0",
                "acceptHeader": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                "deviceExperimentId": "ChxOek14TmpVek16QXpNekE1TlRFNE9ETTVNdz09EIeYpqwGGIeYpqwG",
                "screenWidthPoints": 1536,
                "screenHeightPoints": 338,
                "utcOffsetMinutes": 180,
                "memoryTotalKbytes": "8000000",
                "mainAppWebInfo": {
                    "graftUrl": "/feed/subscriptions",
                    "pwaInstallabilityStatus": "PWA_INSTALLABILITY_STATUS_CAN_BE_INSTALLED",
                    "webDisplayMode": "WEB_DISPLAY_MODE_BROWSER",
                    "isWebNativeShareAvailable": True
                }
            },
            "user": {
                "lockedSafetyMode": False
            },
            "request": {
                "useSsl": True,
                "internalExperimentFlags": [],
                "consistencyTokenJars": []
            },
            "clickTracking": {
                "clickTrackingParams": "CBwQ8qgHGAIiEwiLxa3o4KqDAxWFGtYAHUoYBog="
            },
            "adSignalsInfo": {
                "params": [
                    {
                        "key": "dt",
                        "value": "1703513096807"
                    },
                    {
                        "key": "flash",
                        "value": "0"
                    },
                    {
                        "key": "frm",
                        "value": "0"
                    },
                    {
                        "key": "u_tz",
                        "value": "180"
                    },
                    {
                        "key": "u_his",
                        "value": "17"
                    },
                    {
                        "key": "u_h",
                        "value": "864"
                    },
                    {
                        "key": "u_w",
                        "value": "1536"
                    },
                    {
                        "key": "u_ah",
                        "value": "824"
                    },
                    {
                        "key": "u_aw",
                        "value": "1536"
                    },
                    {
                        "key": "u_cd",
                        "value": "24"
                    },
                    {
                        "key": "bc",
                        "value": "31"
                    },
                    {
                        "key": "bih",
                        "value": "338"
                    },
                    {
                        "key": "biw",
                        "value": "1520"
                    },
                    {
                        "key": "brdim",
                        "value": "0,0,0,0,1536,0,1536,824,1536,338"
                    },
                    {
                        "key": "vis",
                        "value": "1"
                    },
                    {
                        "key": "wgl",
                        "value": "true"
                    },
                    {
                        "key": "ca_type",
                        "value": "image"
                    }
                ]
            }
        },
        "browseId": "FEsubscriptions"
    })
    headers = {
        'authority': 'www.youtube.com',
        'accept': '*/*',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/json',
        'cookie': 'CONSENT=PENDING+917; SOCS=CAISEwgDEgk1ODE3OTQxMTEaAnJ1IAEaBgiAlNCqBg; wide=1; _gcl_au=1.1.1236695019.1702128731; _ga=GA1.1.46170218.1702128973; VISITOR_PRIVACY_METADATA=CgJERRIEEgAgOg%3D%3D; VISITOR_INFO1_LIVE=1uQAro3414g; YSC=mbg-Ztr7WdQ; _ga_VCGEPY40VB=GS1.1.1703510732.9.1.1703512434.0.0.0; GPS=1; PREF=f4=4010000&f6=40000000&tz=Europe.Moscow&f7=100&f5=30000&guide_collapsed=true; ST-1tzw2b8=itct=CBwQ8qgHGAIiEwiLxa3o4KqDAxWFGtYAHUoYBog%3D&csn=MC4yMDE3Nzc0ODkzNjcwNTk4Ng..&endpoint=%7B%22clickTrackingParams%22%3A%22CBwQ8qgHGAIiEwiLxa3o4KqDAxWFGtYAHUoYBog%3D%22%2C%22commandMetadata%22%3A%7B%22webCommandMetadata%22%3A%7B%22url%22%3A%22%2Ffeed%2Fsubscriptions%22%2C%22webPageType%22%3A%22WEB_PAGE_TYPE_BROWSE%22%2C%22rootVe%22%3A96368%2C%22apiUrl%22%3A%22%2Fyoutubei%2Fv1%2Fbrowse%22%7D%7D%2C%22browseEndpoint%22%3A%7B%22browseId%22%3A%22FEsubscriptions%22%7D%7D',
        'origin': 'https://www.youtube.com',
        'referer': 'https://www.youtube.com/feed/subscriptions',
        'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
        'sec-ch-ua-arch': '"x86"',
        'sec-ch-ua-bitness': '"64"',
        'sec-ch-ua-full-version': '"120.0.6099.129"',
        'sec-ch-ua-full-version-list': '"Not_A Brand";v="8.0.0.0", "Chromium";v="120.0.6099.129", "Google Chrome";v="120.0.6099.129"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-model': '""',
        'sec-ch-ua-platform': '"Windows"',
        'sec-ch-ua-platform-version': '"10.0.0"',
        'sec-ch-ua-wow64': '?0',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'same-origin',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'x-client-data': 'CKm1yQEIj7bJAQimtskBCKmdygEIhZbLAQiVocsBCJv+zAEI+ZjNAQiFoM0BCNy9zQEIj+HNAQiu6c0BCN7szQEIoe7NAQjJ7s0BCIPwzQEIhfDNARin6s0B',
        'x-goog-visitor-id': 'CgsxdVFBcm8zNDE0ZyiHmKasBjIKCgJERRIEEgAgOg%3D%3D',
        'x-youtube-bootstrap-logged-in': 'false',
        'x-youtube-client-name': '1',
        'x-youtube-client-version': '2.20231219.04.00'
    }
    return url, payload, headers
#
#
#
#
#


def check_closed_left_menu_you_button_api():
    url = "https://www.youtube.com/youtubei/v1/browse?key=AIzaSyAO_FJ2SlqU8Q4STEHLGCilw_Y9_11qcW8&prettyPrint=false"

    payload = json.dumps({
        "context": {
            "client": {
                "hl": "ru",
                "gl": "US",
                "remoteHost": "162.210.194.38",
                "deviceMake": "",
                "deviceModel": "",
                "visitorData": "CgsxdVFBcm8zNDE0ZyiHmKasBjIKCgJERRIEEgAgOg%3D%3D",
                "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36,gzip(gfe)",
                "clientName": "WEB",
                "clientVersion": "2.20231219.04.00",
                "osName": "Windows",
                "osVersion": "10.0",
                "originalUrl": "https://www.youtube.com/feed/you",
                "screenPixelDensity": 1,
                "platform": "DESKTOP",
                "clientFormFactor": "UNKNOWN_FORM_FACTOR",
                "configInfo": {
                    "appInstallData": "CIeYpqwGEJmUsAUQiIewBRCu1P4SEJT6_hIQ65OuBRC8-a8FEJqksAUQ1YiwBRC3768FENfprwUQyfevBRDnhv8SEM2VsAUQ_Z-wBRC9tq4FENShrwUQieiuBRCZkbAFEPufsAUQvvmvBRDnuq8FENPhrwUQ_IWwBRCmmrAFEOmMsAUQ3IKwBRC9mbAFEKSgsAUQ9fmvBRComrAFEKKBsAUQnouwBRCikrAFEJj8_hIQmvCvBRCst68FEJeDsAUQiOOvBRDd6P4SENqYsAUQ5LP-EhDQjbAFEKagsAUQj6KwBRD6krAFEKuCsAUQ4tSuBRDSlbAFEMzfrgUQzK7-EhDbr68FEOHyrwUQ7qKvBRDHg7AFEPmfsAUQqfevBRC9irAFEKmgsAUQ6-j-EhDZya8FELfq_hIQt52wBRC4i64FEOrDrwUQpcL-EhCoobAFEKaBsAUQ16SwBRDmnrAFEOajsAUQsKWwBQ%3D%3D"
                },
                "screenDensityFloat": 1.25,
                "userInterfaceTheme": "USER_INTERFACE_THEME_DARK",
                "timeZone": "Europe/Moscow",
                "browserName": "Chrome",
                "browserVersion": "120.0.0.0",
                "acceptHeader": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                "deviceExperimentId": "ChxOek14TmpVek16QXpNekE1TlRFNE9ETTVNdz09EIeYpqwGGIeYpqwG",
                "screenWidthPoints": 1536,
                "screenHeightPoints": 426,
                "utcOffsetMinutes": 180,
                "memoryTotalKbytes": "8000000",
                "mainAppWebInfo": {
                    "graftUrl": "/feed/you",
                    "pwaInstallabilityStatus": "PWA_INSTALLABILITY_STATUS_CAN_BE_INSTALLED",
                    "webDisplayMode": "WEB_DISPLAY_MODE_BROWSER",
                    "isWebNativeShareAvailable": True
                }
            },
            "user": {
                "lockedSafetyMode": False
            },
            "request": {
                "useSsl": True,
                "internalExperimentFlags": [],
                "consistencyTokenJars": []
            },
            "clickTracking": {
                "clickTrackingParams": "CBoQ8agHGAAiEwiLxa3o4KqDAxWFGtYAHUoYBog="
            },
            "adSignalsInfo": {
                "params": [
                    {
                        "key": "dt",
                        "value": "1703513096807"
                    },
                    {
                        "key": "flash",
                        "value": "0"
                    },
                    {
                        "key": "frm",
                        "value": "0"
                    },
                    {
                        "key": "u_tz",
                        "value": "180"
                    },
                    {
                        "key": "u_his",
                        "value": "18"
                    },
                    {
                        "key": "u_h",
                        "value": "864"
                    },
                    {
                        "key": "u_w",
                        "value": "1536"
                    },
                    {
                        "key": "u_ah",
                        "value": "824"
                    },
                    {
                        "key": "u_aw",
                        "value": "1536"
                    },
                    {
                        "key": "u_cd",
                        "value": "24"
                    },
                    {
                        "key": "bc",
                        "value": "31"
                    },
                    {
                        "key": "bih",
                        "value": "426"
                    },
                    {
                        "key": "biw",
                        "value": "1520"
                    },
                    {
                        "key": "brdim",
                        "value": "0,0,0,0,1536,0,1536,824,1536,426"
                    },
                    {
                        "key": "vis",
                        "value": "1"
                    },
                    {
                        "key": "wgl",
                        "value": "true"
                    },
                    {
                        "key": "ca_type",
                        "value": "image"
                    }
                ]
            }
        },
        "browseId": "FElibrary",
        "params": "KgN5b3U%3D"
    })
    headers = {
        'authority': 'www.youtube.com',
        'accept': '*/*',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/json',
        'cookie': 'CONSENT=PENDING+917; SOCS=CAISEwgDEgk1ODE3OTQxMTEaAnJ1IAEaBgiAlNCqBg; wide=1; _gcl_au=1.1.1236695019.1702128731; _ga=GA1.1.46170218.1702128973; VISITOR_PRIVACY_METADATA=CgJERRIEEgAgOg%3D%3D; VISITOR_INFO1_LIVE=1uQAro3414g; YSC=mbg-Ztr7WdQ; _ga_VCGEPY40VB=GS1.1.1703510732.9.1.1703512434.0.0.0; GPS=1; PREF=f4=4010000&f6=40000000&tz=Europe.Moscow&f7=100&f5=30000&guide_collapsed=true; ST-ci3gpp=itct=CBoQ8agHGAAiEwiLxa3o4KqDAxWFGtYAHUoYBog%3D&csn=MC44NTU2NzA2NDI2MDU1Njg.&endpoint=%7B%22clickTrackingParams%22%3A%22CBoQ8agHGAAiEwiLxa3o4KqDAxWFGtYAHUoYBog%3D%22%2C%22commandMetadata%22%3A%7B%22webCommandMetadata%22%3A%7B%22url%22%3A%22%2Ffeed%2Fyou%22%2C%22webPageType%22%3A%22WEB_PAGE_TYPE_BROWSE%22%2C%22rootVe%22%3A6827%2C%22apiUrl%22%3A%22%2Fyoutubei%2Fv1%2Fbrowse%22%7D%7D%2C%22browseEndpoint%22%3A%7B%22browseId%22%3A%22FElibrary%22%2C%22params%22%3A%22KgN5b3U%253D%22%7D%7D',
        'origin': 'https://www.youtube.com',
        'referer': 'https://www.youtube.com/feed/you',
        'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
        'sec-ch-ua-arch': '"x86"',
        'sec-ch-ua-bitness': '"64"',
        'sec-ch-ua-full-version': '"120.0.6099.129"',
        'sec-ch-ua-full-version-list': '"Not_A Brand";v="8.0.0.0", "Chromium";v="120.0.6099.129", "Google Chrome";v="120.0.6099.129"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-model': '""',
        'sec-ch-ua-platform': '"Windows"',
        'sec-ch-ua-platform-version': '"10.0.0"',
        'sec-ch-ua-wow64': '?0',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'same-origin',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'x-client-data': 'CKm1yQEIj7bJAQimtskBCKmdygEIhZbLAQiVocsBCJv+zAEI+ZjNAQiFoM0BCNy9zQEIj+HNAQiu6c0BCN7szQEIoe7NAQjJ7s0BCIPwzQEIhfDNARin6s0B',
        'x-goog-visitor-id': 'CgsxdVFBcm8zNDE0ZyiHmKasBjIKCgJERRIEEgAgOg%3D%3D',
        'x-youtube-bootstrap-logged-in': 'false',
        'x-youtube-client-name': '1',
        'x-youtube-client-version': '2.20231219.04.00'
    }
    return url, payload, headers
#
#
#
#
#


def check_closed_left_menu_history_button_api():
    url = "https://www.youtube.com/youtubei/v1/browse?key=AIzaSyAO_FJ2SlqU8Q4STEHLGCilw_Y9_11qcW8&prettyPrint=false"

    payload = json.dumps({
        "context": {
            "client": {
                "hl": "ru",
                "gl": "US",
                "remoteHost": "162.210.194.38",
                "deviceMake": "",
                "deviceModel": "",
                "visitorData": "CgsxdVFBcm8zNDE0ZyiHmKasBjIKCgJERRIEEgAgOg%3D%3D",
                "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36,gzip(gfe)",
                "clientName": "WEB",
                "clientVersion": "2.20231219.04.00",
                "osName": "Windows",
                "osVersion": "10.0",
                "originalUrl": "https://www.youtube.com/feed/history",
                "screenPixelDensity": 1,
                "platform": "DESKTOP",
                "clientFormFactor": "UNKNOWN_FORM_FACTOR",
                "configInfo": {
                    "appInstallData": "CIeYpqwGEJmUsAUQiIewBRCu1P4SEJT6_hIQ65OuBRC8-a8FEJqksAUQ1YiwBRC3768FENfprwUQyfevBRDnhv8SEM2VsAUQ_Z-wBRC9tq4FENShrwUQieiuBRCZkbAFEPufsAUQvvmvBRDnuq8FENPhrwUQ_IWwBRCmmrAFEOmMsAUQ3IKwBRC9mbAFEKSgsAUQ9fmvBRComrAFEKKBsAUQnouwBRCikrAFEJj8_hIQmvCvBRCst68FEJeDsAUQiOOvBRDd6P4SENqYsAUQ5LP-EhDQjbAFEKagsAUQj6KwBRD6krAFEKuCsAUQ4tSuBRDSlbAFEMzfrgUQzK7-EhDbr68FEOHyrwUQ7qKvBRDHg7AFEPmfsAUQqfevBRC9irAFEKmgsAUQ6-j-EhDZya8FELfq_hIQt52wBRC4i64FEOrDrwUQpcL-EhCoobAFEKaBsAUQ16SwBRDmnrAFEOajsAUQsKWwBQ%3D%3D"
                },
                "screenDensityFloat": 1.25,
                "userInterfaceTheme": "USER_INTERFACE_THEME_DARK",
                "timeZone": "Europe/Moscow",
                "browserName": "Chrome",
                "browserVersion": "120.0.0.0",
                "acceptHeader": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                "deviceExperimentId": "ChxOek14TmpVek16QXpNekE1TlRFNE9ETTVNdz09EIeYpqwGGIeYpqwG",
                "screenWidthPoints": 1536,
                "screenHeightPoints": 475,
                "utcOffsetMinutes": 180,
                "memoryTotalKbytes": "8000000",
                "mainAppWebInfo": {
                    "graftUrl": "/feed/history",
                    "pwaInstallabilityStatus": "PWA_INSTALLABILITY_STATUS_CAN_BE_INSTALLED",
                    "webDisplayMode": "WEB_DISPLAY_MODE_BROWSER",
                    "isWebNativeShareAvailable": True
                }
            },
            "user": {
                "lockedSafetyMode": False
            },
            "request": {
                "useSsl": True,
                "internalExperimentFlags": [],
                "consistencyTokenJars": []
            },
            "clickTracking": {
                "clickTrackingParams": "CBkQ5KgHGAEiEwiLxa3o4KqDAxWFGtYAHUoYBog="
            },
            "adSignalsInfo": {
                "params": [
                    {
                        "key": "dt",
                        "value": "1703513096807"
                    },
                    {
                        "key": "flash",
                        "value": "0"
                    },
                    {
                        "key": "frm",
                        "value": "0"
                    },
                    {
                        "key": "u_tz",
                        "value": "180"
                    },
                    {
                        "key": "u_his",
                        "value": "19"
                    },
                    {
                        "key": "u_h",
                        "value": "864"
                    },
                    {
                        "key": "u_w",
                        "value": "1536"
                    },
                    {
                        "key": "u_ah",
                        "value": "824"
                    },
                    {
                        "key": "u_aw",
                        "value": "1536"
                    },
                    {
                        "key": "u_cd",
                        "value": "24"
                    },
                    {
                        "key": "bc",
                        "value": "31"
                    },
                    {
                        "key": "bih",
                        "value": "475"
                    },
                    {
                        "key": "biw",
                        "value": "1520"
                    },
                    {
                        "key": "brdim",
                        "value": "0,0,0,0,1536,0,1536,824,1536,475"
                    },
                    {
                        "key": "vis",
                        "value": "1"
                    },
                    {
                        "key": "wgl",
                        "value": "true"
                    },
                    {
                        "key": "ca_type",
                        "value": "image"
                    }
                ]
            }
        },
        "browseId": "FEhistory"
    })
    headers = {
        'authority': 'www.youtube.com',
        'accept': '*/*',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/json',
        'cookie': 'CONSENT=PENDING+917; SOCS=CAISEwgDEgk1ODE3OTQxMTEaAnJ1IAEaBgiAlNCqBg; wide=1; _gcl_au=1.1.1236695019.1702128731; _ga=GA1.1.46170218.1702128973; VISITOR_PRIVACY_METADATA=CgJERRIEEgAgOg%3D%3D; VISITOR_INFO1_LIVE=1uQAro3414g; YSC=mbg-Ztr7WdQ; _ga_VCGEPY40VB=GS1.1.1703510732.9.1.1703512434.0.0.0; GPS=1; PREF=f4=4010000&f6=40000000&tz=Europe.Moscow&f7=100&f5=30000&guide_collapsed=true; ST-cv3kr6=itct=CBkQ5KgHGAEiEwiLxa3o4KqDAxWFGtYAHUoYBog%3D&csn=MC4yMzYxNjYwOTU1MzEwOTQwMg..&endpoint=%7B%22clickTrackingParams%22%3A%22CBkQ5KgHGAEiEwiLxa3o4KqDAxWFGtYAHUoYBog%3D%22%2C%22commandMetadata%22%3A%7B%22webCommandMetadata%22%3A%7B%22url%22%3A%22%2Ffeed%2Fhistory%22%2C%22webPageType%22%3A%22WEB_PAGE_TYPE_BROWSE%22%2C%22rootVe%22%3A6827%2C%22apiUrl%22%3A%22%2Fyoutubei%2Fv1%2Fbrowse%22%7D%7D%2C%22browseEndpoint%22%3A%7B%22browseId%22%3A%22FEhistory%22%7D%7D',
        'origin': 'https://www.youtube.com',
        'referer': 'https://www.youtube.com/feed/history',
        'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
        'sec-ch-ua-arch': '"x86"',
        'sec-ch-ua-bitness': '"64"',
        'sec-ch-ua-full-version': '"120.0.6099.129"',
        'sec-ch-ua-full-version-list': '"Not_A Brand";v="8.0.0.0", "Chromium";v="120.0.6099.129", "Google Chrome";v="120.0.6099.129"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-model': '""',
        'sec-ch-ua-platform': '"Windows"',
        'sec-ch-ua-platform-version': '"10.0.0"',
        'sec-ch-ua-wow64': '?0',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'same-origin',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'x-client-data': 'CKm1yQEIj7bJAQimtskBCKmdygEIhZbLAQiVocsBCJv+zAEI+ZjNAQiFoM0BCNy9zQEIj+HNAQiu6c0BCN7szQEIoe7NAQjJ7s0BCIPwzQEIhfDNARin6s0B',
        'x-goog-visitor-id': 'CgsxdVFBcm8zNDE0ZyiHmKasBjIKCgJERRIEEgAgOg%3D%3D',
        'x-youtube-bootstrap-logged-in': 'false',
        'x-youtube-client-name': '1',
        'x-youtube-client-version': '2.20231219.04.00'
    }
    return url, payload, headers