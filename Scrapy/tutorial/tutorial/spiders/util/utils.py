from urllib.parse import quote


def construct_url(cate_id, gender):
    url = 'https://www.zalora.com.hk/_c/v1/desktop/list_catalog_full?params='
    url += quote(str({"url": "/men/clothing", "q": "", "sort": "popularity", "dir": "desc", "offset": 0, "limit": 99,
                      "category_id": [str(cate_id)], "range": [], "occasion": [], "material_composition": [],
                      "pattern": [],
                      "campaign_categoryId": [], "color": [], "sizesystem": [], "brand": [], "age_group": [],
                      "gender": [gender], "price": "", "normalized_sell_through": "", "segment": gender,
                      "special_price": False, "all_products": False, "new_products": False, "top_sellers": False,
                      "catalogtype": "Main", "campaign": "", "discount": "", "age": "", "mp": "", "or": "",
                      "shipment_type": "", "exs": "", "lang": "en", "is_brunei": False, "sort_formula": "",
                      "rerank_formula": "", "search_suggest": False,
                      "custom_filters": {"filter1": "", "filter2": "", "filter3": "", "filter4": ""}, "elevate_ids": [],
                      "user_id": "", "enable_visual_sort": True, "enable_filter_ads": True,
                      "features": {"compact_catalog_desktop": False, "name_search": False, "solr7_support": True,
                                   "pick_for_you": False, "learn_to_sort_catalog": False}, "onsite_filters": {},
                      "user_query": "", "is_multiple_source": True}))
    return url.replace('%27', '"')