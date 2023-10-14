import requests
import json

def search_safeway(search_query):
    # Base URL
    base_url = "https://www.safeway.com/abs/pub/xapi/pgmsearch/v1/search/products"
    
    # Parameters
    params = {
        'request-id': '8261697238354967169',
        'url': 'https://www.safeway.com',
        'pageurl': 'https://www.safeway.com',
        'pagename': 'search',
        'rows': '30',
        'start': '0',
        'search-type': 'keyword',
        'storeid': '3132',
        'featured': 'true',
        'search-uid': 'uid=2697982967044:v=15.0:ts=1694851634725:hc=7',
        'q': search_query,
        'sort': '',
        'featuredsessionid': '',
        'screenwidth': '1234',
        'dvid': 'web-4.1search',
        'channel': 'instore',
        'cross-seller-max-count': '14',
        'wineshopstoreid': '5799',
        'wineshopwidgetid': 'nlvkox9e',
        'timezone': 'America/Los_Angeles',
        'zipcode': '94611',
        'variant': 'ACIP15567_b',
        'visitorId': '5d75564f-2ef8-4a04-b5bb-eabc15cd7309',
        'pgm': 'mkp-crossseller,wineshop',
        'banner': 'safeway'
    }
    
    # Headers
    headers = {
        'authority': 'www.safeway.com',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'cookie': 'visid_incap_1610353=qFPTrrWQQreHXImD90cT0y5iBWUAAAAAQUIPAAAAAAAJXNb1qwNAldLE0R+FFqng; __pr.vco1py=3H72l0jfXH; nlbi_1610353=EVsLP1XoZxI4Mv9v6eNT2gAAAABhe2NZBWcFe6PeSg3Nao6z; AMCVS_A7BF3BC75245ADF20A490D4D%40AdobeOrg=1; ECommBanner=safeway; ECommSignInCount=0; at_check=true; SAFEWAY_MODAL_LINK=; __pdst=83beec7b58774a48bc79051b4875a965; absVisitorId=5d75564f-2ef8-4a04-b5bb-eabc15cd7309; s_sq=%5B%5BB%5D%5D; abs_gsession=%7B%22info%22%3A%7B%22COMMON%22%3A%7B%22Selection%22%3A%22user%22%2C%22preference%22%3A%22J4U%22%2C%22userType%22%3A%22G%22%2C%22zipcode%22%3A%2294611%22%2C%22banner%22%3A%22safeway%22%2C%22siteType%22%3A%22C%22%2C%22customerType%22%3A%22%22%7D%2C%22J4U%22%3A%7B%22zipcode%22%3A%2294611%22%2C%22storeId%22%3A%223132%22%7D%2C%22SHOP%22%3A%7B%22zipcode%22%3A%2294611%22%2C%22storeId%22%3A%223132%22%7D%7D%7D; abs_previouslogin=%7B%22info%22%3A%7B%22COMMON%22%3A%7B%22Selection%22%3A%22user%22%2C%22preference%22%3A%22J4U%22%2C%22userType%22%3A%22G%22%2C%22zipcode%22%3A%2294611%22%2C%22banner%22%3A%22safeway%22%2C%22siteType%22%3A%22C%22%2C%22customerType%22%3A%22%22%7D%2C%22J4U%22%3A%7B%22zipcode%22%3A%2294611%22%2C%22storeId%22%3A%223132%22%7D%2C%22SHOP%22%3A%7B%22zipcode%22%3A%2294611%22%2C%22storeId%22%3A%223132%22%7D%7D%7D; _br_uid_2=uid%3D2697982967044%3Av%3D15.0%3Ats%3D1694851634725%3Ahc%3D8; incap_ses_567_1610353=xZxxFkcuDy8Zkb0OhmTeB4vbKWUAAAAAIP4BoVMAU3eJTabOZkMA6w==; nlbi_1610353_2147483392=x8eNG2f3fz1hzrEK6eNT2gAAAADyv4vY9m7MRbmBAbSiYieG; reese84=3:OPlCX0YA/Tr/FetEQjPBRg==:uazfO7vkBBsDM1aeYfQv/Myf+AbYjBWpXLdeSMIpbKjaXmTv3FMzVewoTBHJTIikIr3uUJ1rYqjYlegWYaEDVr8v61zZ/FCkTO0QtTLUVyu0TLN0clpnT6VSjLj/mek8aGIWZ1xdQwNSNxS4GoxztHyUojtxcb2yfe+d2Aw9YghdpN23WmGTJcRVUe2Bx5AfW8/psjpVY8RXzSx6vF32CgOzeDwtb/F2EnezcE4WLXv1l0TKTpTKd6YtxL+C9U9wbNj5MP1t3a5Foy35HNxuEI5ZwQs7qstIM/FrIWoBIUk7jVxvWN1bTqq17NxR9fg8jL6MKloyu7h0STRT0LNTUcDxU+zY4N3BOKACaTVwcsqzEMg44Rf3BcHXv0QJL5u4yOuPem3Q7IrERskxssK1P96CJolQhgjfe5rSyRSSi3sIk00IX/OokNuRcjHM+cbAIKOVCVXOUg/8szvdsohRgQ==:I5bNwGY84dvSuZlsVNeLA4xrBdZ5IVmlaEU/YmpvaEk=; _dd_s=; SWY_SYND_USER_INFO=%7B%22storeAddress%22%3A%22%22%2C%22storeZip%22%3A%2294611%22%2C%22storeId%22%3A%223132%22%2C%22preference%22%3A%22J4U%22%7D; AMCV_A7BF3BC75245ADF20A490D4D%40AdobeOrg=179643557%7CMCIDTS%7C19644%7CMCMID%7C36900911009963716133469027599985990337%7CMCAAMLH-1697847656%7C9%7CMCAAMB-1697847656%7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y%7CMCOPTOUT-1697250056s%7CNONE%7CvVersion%7C5.5.0; SWY_SHARED_SESSION_INFO=%7B%22info%22%3A%7B%22COMMON%22%3A%7B%22Selection%22%3A%22user%22%2C%22preference%22%3A%22J4U%22%2C%22userType%22%3A%22G%22%2C%22zipcode%22%3A%2294611%22%2C%22banner%22%3A%22safeway%22%2C%22siteType%22%3A%22C%22%2C%22customerType%22%3A%22%22%2C%22wfcStoreId%22%3A5799%7D%2C%22J4U%22%3A%7B%22zipcode%22%3A%2294611%22%2C%22storeId%22%3A%223132%22%7D%2C%22SHOP%22%3A%7B%22zipcode%22%3A%2294611%22%2C%22storeId%22%3A%223132%22%7D%7D%7D; mbox=PC#289373610e244d35ad348b678585ad39.35_0#1760487657|session#2daf0a6c02e447af8b90848e9759ae8c#1697244717; OptanonConsent=isGpcEnabled=0&datestamp=Fri+Oct+13+2023+17%3A20%3A56+GMT-0700+(Pacific+Daylight+Time)&version=202306.2.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=49e494aa-699f-492e-bdf0-d9e73f774e8e&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0004%3A1%2CC0003%3A1&AwaitingReconsent=false',
        'ocp-apim-subscription-key': '5e790236c84e46338f4290aa1050cdd4',
        'referer': 'https://www.safeway.com/shop/search-results.html?q=' + search_query,
        'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'
    }
    
    # Make the request
    response = requests.get(base_url, headers=headers, params=params)
    
    # Check the response status and return the result
    if response.status_code == 200:
        return response.json()
    else:
        return f"Error: Unable to fetch the data. Status code: {response.status_code}"

