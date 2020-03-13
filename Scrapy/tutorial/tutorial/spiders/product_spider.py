import json
import time

import scrapy

from tutorial.spiders.util.utils import construct_url

data = [
  {
    "label": "Men",
    "value": "B___",
    "category_id": 0,
    "url": [
      "men"
    ],
    "depth": 1,
    "children": [
      {
        "label": "Men's Clothing",
        "value": "BA__",
        "category_id": 26,
        "url": [
          "men",
          "clothing"
        ],
        "depth": 2,
        "children": []
      },
      {
        "label": "Men's Shoes",
        "value": "BB__",
        "category_id": 27,
        "url": [
          "men",
          "shoes"
        ],
        "depth": 2,
        "children": [
          {
            "label": "Sneakers",
            "value": "BBA_",
            "category_id": 413,
            "url": [
              "men",
              "shoes",
              "sneakers-plimsolls"
            ],
            "depth": 3,
            "children": []
          },
          {
            "label": "Loafers & Boat Shoes",
            "value": "BBB_",
            "category_id": 995,
            "url": [
              "men",
              "shoes",
              "loafers-boat-shoes"
            ],
            "depth": 3,
            "children": []
          },
          {
            "label": "Slip-Ons",
            "value": "BBC_",
            "category_id": 412,
            "url": [
              "men",
              "shoes",
              "slip-ons"
            ],
            "depth": 3,
            "children": []
          },
          {
            "label": "Formal",
            "value": "BBD_",
            "category_id": 2004,
            "url": [
              "men",
              "shoes",
              "formal-shoes"
            ],
            "depth": 3,
            "children": []
          },
          {
            "label": "Sandals & Flip Flops",
            "value": "BBE_",
            "category_id": 5369,
            "url": [
              "men",
              "shoes",
              "sandals-flip-flops"
            ],
            "depth": 3,
            "children": [
              {
                "label": "Sandals",
                "value": "BBEA",
                "category_id": 2005,
                "url": [
                  "men",
                  "shoes",
                  "sandals"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Flip Flops",
                "value": "BBEB",
                "category_id": 2006,
                "url": [
                  "men",
                  "shoes",
                  "flip-flops"
                ],
                "depth": 4,
                "children": []
              }
            ]
          },
          {
            "label": "Boots",
            "value": "BBF_",
            "category_id": 171,
            "url": [
              "men",
              "shoes",
              "boots"
            ],
            "depth": 3,
            "children": []
          },
          {
            "label": "Sports Shoes",
            "value": "BBG_",
            "category_id": 416,
            "url": [
              "men",
              "shoes",
              "sports-shoes"
            ],
            "depth": 3,
            "children": []
          },
          {
            "label": "Shoes Accessories",
            "value": "BBH_",
            "category_id": 5778,
            "url": [
              "men",
              "shoes",
              "shoes-accessories"
            ],
            "depth": 3,
            "children": []
          }
        ]
      },
      {
        "label": "Men's Accessories",
        "value": "BC__",
        "category_id": 257,
        "url": [
          "men",
          "accessories"
        ],
        "depth": 2,
        "children": [
          {
            "label": "Watches",
            "value": "BCA_",
            "category_id": 3243,
            "url": [
              "men",
              "accessories",
              "watches"
            ],
            "depth": 3,
            "children": [
              {
                "label": "Analogue Watches",
                "value": "BCAA",
                "category_id": 3257,
                "url": [
                  "men",
                  "accessories",
                  "analogue-watches"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Digital Watches",
                "value": "BCAB",
                "category_id": 3256,
                "url": [
                  "men",
                  "accessories",
                  "digital-watches"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Sports Watches",
                "value": "BCAC",
                "category_id": 3255,
                "url": [
                  "men",
                  "accessories",
                  "sports-watches"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Casual Watches",
                "value": "BCAD",
                "category_id": 4818,
                "url": [
                  "men",
                  "accessories",
                  "casual-watches"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Dress Watches",
                "value": "BCAE",
                "category_id": 4819,
                "url": [
                  "men",
                  "accessories",
                  "dress-watches"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Chronograph Watches",
                "value": "BCAF",
                "category_id": 4813,
                "url": [
                  "men",
                  "accessories",
                  "chronograph-watches"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Smart Watches",
                "value": "BCAG",
                "category_id": 5782,
                "url": [
                  "men",
                  "accessories",
                  "smart-watches"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Shop by Strap",
                "value": "BCAH",
                "category_id": 4814,
                "url": [
                  "men",
                  "accessories",
                  "shop-by-strap"
                ],
                "depth": 4,
                "children": []
              }
            ]
          },
          {
            "label": "Eyewear",
            "value": "BCB_",
            "category_id": 6716,
            "url": [
              "men",
              "accessories",
              "eyeglasses"
            ],
            "depth": 3,
            "children": [
              {
                "label": "Sunglasses",
                "value": "BCBA",
                "category_id": 1041,
                "url": [
                  "men",
                  "accessories",
                  "sunglasses"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Glasses",
                "value": "BCBB",
                "category_id": 4603,
                "url": [
                  "men",
                  "accessories",
                  "glasses"
                ],
                "depth": 4,
                "children": []
              }
            ]
          },
          {
            "label": "Wallets",
            "value": "BCC_",
            "category_id": 322,
            "url": [
              "men",
              "accessories",
              "wallets"
            ],
            "depth": 3,
            "children": [
              {
                "label": "Non-Leather Wallets",
                "value": "BCCA",
                "category_id": 2148,
                "url": [
                  "men",
                  "accessories",
                  "non-leather-wallets"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Leather Wallets",
                "value": "BCCB",
                "category_id": 2147,
                "url": [
                  "men",
                  "accessories",
                  "leather-wallets"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Billfolds & Money Clips",
                "value": "BCCC",
                "category_id": 5360,
                "url": [
                  "men",
                  "accessories",
                  "billfolds-money-clips"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Card Holders",
                "value": "BCCD",
                "category_id": 323,
                "url": [
                  "men",
                  "accessories",
                  "card-holders"
                ],
                "depth": 4,
                "children": []
              }
            ]
          },
          {
            "label": "Belts",
            "value": "BCD_",
            "category_id": 326,
            "url": [
              "men",
              "accessories",
              "belts"
            ],
            "depth": 3,
            "children": [
              {
                "label": "Non-Leather Belts",
                "value": "BCDA",
                "category_id": 2149,
                "url": [
                  "men",
                  "accessories",
                  "non-leather-belts"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Canvas Belts",
                "value": "BCDB",
                "category_id": 328,
                "url": [
                  "men",
                  "accessories",
                  "canvas-belts"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Leather Belts",
                "value": "BCDC",
                "category_id": 327,
                "url": [
                  "men",
                  "accessories",
                  "leather-belts"
                ],
                "depth": 4,
                "children": []
              }
            ]
          },
          {
            "label": "Ties & Accessories",
            "value": "BCE_",
            "category_id": 354,
            "url": [
              "men",
              "accessories",
              "ties-accessories"
            ],
            "depth": 3,
            "children": [
              {
                "label": "Pocket Squares",
                "value": "BCEA",
                "category_id": 6710,
                "url": [
                  "men",
                  "accessories",
                  "pocket-squares"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Cufflinks & Tie Clips",
                "value": "BCEB",
                "category_id": 357,
                "url": [
                  "men",
                  "accessories",
                  "cufflinks-tie-clips"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Bow Ties",
                "value": "BCEC",
                "category_id": 356,
                "url": [
                  "men",
                  "accessories",
                  "bow-ties"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Ties",
                "value": "BCED",
                "category_id": 355,
                "url": [
                  "men",
                  "accessories",
                  "ties"
                ],
                "depth": 4,
                "children": []
              }
            ]
          },
          {
            "label": "Hats & Caps",
            "value": "BCF_",
            "category_id": 329,
            "url": [
              "men",
              "accessories",
              "hats-and-caps"
            ],
            "depth": 3,
            "children": [
              {
                "label": "Beanies",
                "value": "BCFA",
                "category_id": 332,
                "url": [
                  "men",
                  "accessories",
                  "beanies"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Caps",
                "value": "BCFB",
                "category_id": 331,
                "url": [
                  "men",
                  "accessories",
                  "caps"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Hats",
                "value": "BCFC",
                "category_id": 330,
                "url": [
                  "men",
                  "accessories",
                  "hats"
                ],
                "depth": 4,
                "children": []
              }
            ]
          },
          {
            "label": "Jewellery",
            "value": "BCG_",
            "category_id": 304,
            "url": [
              "men",
              "accessories",
              "jewellery"
            ],
            "depth": 3,
            "children": [
              {
                "label": "Bracelets",
                "value": "BCGA",
                "category_id": 3348,
                "url": [
                  "men",
                  "accessories",
                  "bracelets"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Rings",
                "value": "BCGB",
                "category_id": 314,
                "url": [
                  "men",
                  "accessories",
                  "rings"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Necklaces",
                "value": "BCGC",
                "category_id": 305,
                "url": [
                  "men",
                  "accessories",
                  "necklaces"
                ],
                "depth": 4,
                "children": []
              }
            ]
          },
          {
            "label": "Scarves & Shawls",
            "value": "BCH_",
            "category_id": 408,
            "url": [
              "men",
              "accessories",
              "scarves-shawls"
            ],
            "depth": 3,
            "children": []
          },
          {
            "label": "Technology",
            "value": "BCI_",
            "category_id": 340,
            "url": [
              "men",
              "accessories",
              "technology"
            ],
            "depth": 3,
            "children": [
              {
                "label": "Gadgets & Accessories",
                "value": "BCIA",
                "category_id": 6761,
                "url": [
                  "men",
                  "accessories",
                  "gadgets-accessories"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Laptop Bags & Sleeves",
                "value": "BCIB",
                "category_id": 979,
                "url": [
                  "men",
                  "accessories",
                  "laptop-bags-sleeves"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Phone & Tablet Cases",
                "value": "BCIC",
                "category_id": 342,
                "url": [
                  "men",
                  "accessories",
                  "phone-tablet-cases"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Headphones & Headsets",
                "value": "BCID",
                "category_id": 341,
                "url": [
                  "men",
                  "accessories",
                  "headphones-headsets"
                ],
                "depth": 4,
                "children": []
              }
            ]
          }
        ]
      },
      {
        "label": "Men's Bags",
        "value": "BD__",
        "category_id": 315,
        "url": [
          "men",
          "bags"
        ],
        "depth": 2,
        "children": [
          {
            "label": "Tote Bags",
            "value": "BDA_",
            "category_id": 2155,
            "url": [
              "men",
              "bags",
              "totes"
            ],
            "depth": 3,
            "children": []
          },
          {
            "label": "Laptop Bags",
            "value": "BDB_",
            "category_id": 483,
            "url": [
              "men",
              "bags",
              "laptop-bags"
            ],
            "depth": 3,
            "children": []
          },
          {
            "label": "Messenger Bags",
            "value": "BDC_",
            "category_id": 320,
            "url": [
              "men",
              "bags",
              "messenger"
            ],
            "depth": 3,
            "children": []
          },
          {
            "label": "Travel Bags",
            "value": "BDD_",
            "category_id": 318,
            "url": [
              "men",
              "bags",
              "travel"
            ],
            "depth": 3,
            "children": [
              {
                "label": "Belt Bags",
                "value": "BDDA",
                "category_id": 6752,
                "url": [
                  "men",
                  "bags",
                  "belt-bags"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Wheeled Luggage",
                "value": "BDDB",
                "category_id": 4742,
                "url": [
                  "men",
                  "bags",
                  "wheeled-luggage"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Travel Backpacks",
                "value": "BDDC",
                "category_id": 4741,
                "url": [
                  "men",
                  "bags",
                  "travel-backpacks"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Travel Accessories",
                "value": "BDDD",
                "category_id": 4740,
                "url": [
                  "men",
                  "bags",
                  "travel-accessories"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Hand Luggage",
                "value": "BDDE",
                "category_id": 4739,
                "url": [
                  "men",
                  "bags",
                  "hand-luggage"
                ],
                "depth": 4,
                "children": []
              }
            ]
          },
          {
            "label": "Backpacks",
            "value": "BDE_",
            "category_id": 317,
            "url": [
              "men",
              "bags",
              "backpack"
            ],
            "depth": 3,
            "children": [
              {
                "label": "Plain Backpacks",
                "value": "BDEA",
                "category_id": 6751,
                "url": [
                  "men",
                  "bags",
                  "plain-backpacks"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Printed Backpacks",
                "value": "BDEB",
                "category_id": 6750,
                "url": [
                  "men",
                  "bags",
                  "printed-backpacks"
                ],
                "depth": 4,
                "children": []
              }
            ]
          },
          {
            "label": "Duffel Bags",
            "value": "BDF_",
            "category_id": 5340,
            "url": [
              "men",
              "bags",
              "duffle-bags"
            ],
            "depth": 3,
            "children": []
          },
          {
            "label": "Briefcases",
            "value": "BDG_",
            "category_id": 319,
            "url": [
              "men",
              "bags",
              "briefcases"
            ],
            "depth": 3,
            "children": []
          }
        ]
      },
      {
        "label": "Men's Sports",
        "value": "BE__",
        "category_id": 471,
        "url": [
          "men",
          "sports"
        ],
        "depth": 2,
        "children": [
          {
            "label": "Shop by Category",
            "value": "BEA_",
            "category_id": 6722,
            "url": [
              "men",
              "sports",
              "shop-by-category"
            ],
            "depth": 3,
            "children": [
              {
                "label": "Clothing",
                "value": "BEAA",
                "category_id": 470,
                "url": [
                  "men",
                  "sports",
                  "clothing"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Shoes",
                "value": "BEAB",
                "category_id": 557,
                "url": [
                  "men",
                  "sports",
                  "shoes"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Bags & Backpacks",
                "value": "BEAC",
                "category_id": 2271,
                "url": [
                  "men",
                  "sports",
                  "bags-backpacks"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Accessories",
                "value": "BEAD",
                "category_id": 568,
                "url": [
                  "men",
                  "sports",
                  "accessories"
                ],
                "depth": 4,
                "children": []
              }
            ]
          },
          {
            "label": "Shop by Sport Activity",
            "value": "BEB_",
            "category_id": 6721,
            "url": [
              "men",
              "sports",
              "shop-by-activity"
            ],
            "depth": 3,
            "children": [
              {
                "label": "Training",
                "value": "BEBA",
                "category_id": 5872,
                "url": [
                  "men",
                  "sports",
                  "training"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Running",
                "value": "BEBB",
                "category_id": 5883,
                "url": [
                  "men",
                  "sports",
                  "running"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Lifestyle",
                "value": "BEBC",
                "category_id": 5900,
                "url": [
                  "men",
                  "sports",
                  "lifestyle"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Outdoors",
                "value": "BEBD",
                "category_id": 6782,
                "url": [
                  "men",
                  "sports",
                  "outdoors"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Swim & Beachwear",
                "value": "BEBE",
                "category_id": 5895,
                "url": [
                  "men",
                  "sports",
                  "swim-beachwear"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Team Sports",
                "value": "BEBF",
                "category_id": 6783,
                "url": [
                  "men",
                  "sports",
                  "team-sports"
                ],
                "depth": 4,
                "children": []
              }
            ]
          }
        ]
      },
      {
        "label": "Men's Grooming",
        "value": "BF__",
        "category_id": 5481,
        "url": [
          "men",
          "grooming"
        ],
        "depth": 2,
        "children": [
          {
            "label": "Shaving",
            "value": "BFA_",
            "category_id": 5627,
            "url": [
              "men",
              "grooming",
              "shaving"
            ],
            "depth": 3,
            "children": [
              {
                "label": "Post-Shaving",
                "value": "BFAA",
                "category_id": 5630,
                "url": [
                  "men",
                  "grooming",
                  "post-shaving"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Shaving Tools",
                "value": "BFAB",
                "category_id": 5629,
                "url": [
                  "men",
                  "grooming",
                  "shaving-tools"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Pre-Shaving",
                "value": "BFAC",
                "category_id": 5628,
                "url": [
                  "men",
                  "grooming",
                  "pre-shaving"
                ],
                "depth": 4,
                "children": []
              }
            ]
          },
          {
            "label": "Body",
            "value": "BFB_",
            "category_id": 5624,
            "url": [
              "men",
              "grooming",
              "body"
            ],
            "depth": 3,
            "children": [
              {
                "label": "Bath & Shower",
                "value": "BFBA",
                "category_id": 5626,
                "url": [
                  "men",
                  "grooming",
                  "bath-shower"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Body Lotion & Treatments",
                "value": "BFBB",
                "category_id": 5625,
                "url": [
                  "men",
                  "grooming",
                  "body-lotion-treatments"
                ],
                "depth": 4,
                "children": []
              }
            ]
          },
          {
            "label": "Skin Care",
            "value": "BFC_",
            "category_id": 5620,
            "url": [
              "men",
              "grooming",
              "skin-care"
            ],
            "depth": 3,
            "children": [
              {
                "label": "Eye cream",
                "value": "BFCA",
                "category_id": 5623,
                "url": [
                  "men",
                  "grooming",
                  "eye-cream"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Moisturizer and Treatments",
                "value": "BFCB",
                "category_id": 5622,
                "url": [
                  "men",
                  "grooming",
                  "moisturizer-treatments"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Cleansers",
                "value": "BFCC",
                "category_id": 5621,
                "url": [
                  "men",
                  "grooming",
                  "cleansers"
                ],
                "depth": 4,
                "children": []
              }
            ]
          },
          {
            "label": "Hair Care",
            "value": "BFD_",
            "category_id": 5617,
            "url": [
              "men",
              "grooming",
              "hair-care"
            ],
            "depth": 3,
            "children": [
              {
                "label": "Shampoo & Conditioner",
                "value": "BFDA",
                "category_id": 5619,
                "url": [
                  "men",
                  "grooming",
                  "shampoo-conditioner"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Styling",
                "value": "BFDB",
                "category_id": 5618,
                "url": [
                  "men",
                  "grooming",
                  "styling"
                ],
                "depth": 4,
                "children": []
              }
            ]
          },
          {
            "label": "Fragrance",
            "value": "BFE_",
            "category_id": 5616,
            "url": [
              "men",
              "grooming",
              "fragrance"
            ],
            "depth": 3,
            "children": []
          },
          {
            "label": "Gift Sets",
            "value": "BFF_",
            "category_id": 5615,
            "url": [
              "men",
              "grooming",
              "gift-sets"
            ],
            "depth": 3,
            "children": []
          }
        ]
      },
      {
        "label": "Men's Premium",
        "value": "BG__",
        "category_id": 5987,
        "url": [
          "men",
          "premium"
        ],
        "depth": 2,
        "children": [
          {
            "label": "Clothing",
            "value": "BGA_",
            "category_id": 5994,
            "url": [
              "men",
              "premium",
              "clothing"
            ],
            "depth": 3,
            "children": [
              {
                "label": "T-shirts",
                "value": "BGAA",
                "category_id": 6478,
                "url": [
                  "men",
                  "premium",
                  "t-shirts"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Shirts",
                "value": "BGAB",
                "category_id": 6477,
                "url": [
                  "men",
                  "premium",
                  "shirts"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Polos",
                "value": "BGAC",
                "category_id": 6476,
                "url": [
                  "men",
                  "premium",
                  "polos"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Pants",
                "value": "BGAD",
                "category_id": 6475,
                "url": [
                  "men",
                  "premium",
                  "pants"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Shorts",
                "value": "BGAE",
                "category_id": 6474,
                "url": [
                  "men",
                  "premium",
                  "shorts"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Jeans",
                "value": "BGAF",
                "category_id": 6473,
                "url": [
                  "men",
                  "premium",
                  "jeans"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Beachwear",
                "value": "BGAG",
                "category_id": 6472,
                "url": [
                  "men",
                  "premium",
                  "beachwear"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Underwear & Sleepwear",
                "value": "BGAH",
                "category_id": 6471,
                "url": [
                  "men",
                  "premium",
                  "underwear-sleepwear"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Ethnic Wear",
                "value": "BGAI",
                "category_id": 6470,
                "url": [
                  "men",
                  "premium",
                  "ethnic-wear"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Socks",
                "value": "BGAJ",
                "category_id": 6469,
                "url": [
                  "men",
                  "premium",
                  "socks"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Outerwear",
                "value": "BGAK",
                "category_id": 6842,
                "url": [
                  "men",
                  "premium",
                  "outerwear"
                ],
                "depth": 4,
                "children": []
              }
            ]
          },
          {
            "label": "Shoes",
            "value": "BGB_",
            "category_id": 5993,
            "url": [
              "men",
              "premium",
              "shoes"
            ],
            "depth": 3,
            "children": [
              {
                "label": "Sneakers",
                "value": "BGBA",
                "category_id": 6485,
                "url": [
                  "men",
                  "premium",
                  "sneakers"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Loafers & Boat Shoes",
                "value": "BGBB",
                "category_id": 6484,
                "url": [
                  "men",
                  "premium",
                  "loafers-boat-shoes"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Formal",
                "value": "BGBC",
                "category_id": 6483,
                "url": [
                  "men",
                  "premium",
                  "formal-shoes"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Boots",
                "value": "BGBD",
                "category_id": 6482,
                "url": [
                  "men",
                  "premium",
                  "boots"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Sandals & Flip Flops",
                "value": "BGBE",
                "category_id": 6481,
                "url": [
                  "men",
                  "premium",
                  "sandals-flip-flops"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Slip-Ons",
                "value": "BGBF",
                "category_id": 6479,
                "url": [
                  "men",
                  "premium",
                  "slip-ons"
                ],
                "depth": 4,
                "children": []
              }
            ]
          },
          {
            "label": "Accessories",
            "value": "BGC_",
            "category_id": 5992,
            "url": [
              "men",
              "premium",
              "accessories"
            ],
            "depth": 3,
            "children": [
              {
                "label": "Bags",
                "value": "BGCA",
                "category_id": 6496,
                "url": [
                  "men",
                  "premium",
                  "bags"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Watches",
                "value": "BGCB",
                "category_id": 6495,
                "url": [
                  "men",
                  "premium",
                  "watches"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Eyewear",
                "value": "BGCC",
                "category_id": 6494,
                "url": [
                  "men",
                  "premium",
                  "eyewear"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Wallets",
                "value": "BGCD",
                "category_id": 6493,
                "url": [
                  "men",
                  "premium",
                  "wallets"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Belts",
                "value": "BGCE",
                "category_id": 6492,
                "url": [
                  "men",
                  "premium",
                  "belts"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Travel",
                "value": "BGCF",
                "category_id": 6491,
                "url": [
                  "men",
                  "premium",
                  "travel"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Hats",
                "value": "BGCG",
                "category_id": 6489,
                "url": [
                  "men",
                  "premium",
                  "hats"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Jewellery",
                "value": "BGCH",
                "category_id": 6488,
                "url": [
                  "men",
                  "premium",
                  "jewellery"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Scarves & Shawls",
                "value": "BGCI",
                "category_id": 6487,
                "url": [
                  "men",
                  "premium",
                  "scarves-shawls"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Others",
                "value": "BGCJ",
                "category_id": 6486,
                "url": [
                  "men",
                  "premium",
                  "others-accessories"
                ],
                "depth": 4,
                "children": []
              }
            ]
          },
          {
            "label": "Sports",
            "value": "BGD_",
            "category_id": 5990,
            "url": [
              "men",
              "premium",
              "sports"
            ],
            "depth": 3,
            "children": [
              {
                "label": "Clothing",
                "value": "BGDA",
                "category_id": 6509,
                "url": [
                  "men",
                  "premium",
                  "sports-clothing"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Running",
                "value": "BGDB",
                "category_id": 6589,
                "url": [
                  "men",
                  "premium",
                  "sports-footwear-running"
                ],
                "depth": 5,
                "children": []
              },
              {
                "label": "Lifestyle",
                "value": "BGDC",
                "category_id": 6586,
                "url": [
                  "men",
                  "premium",
                  "sports-footwear-lifestyle"
                ],
                "depth": 5,
                "children": []
              },
              {
                "label": "Sandals & Flip-Flops",
                "value": "BGDD",
                "category_id": 6584,
                "url": [
                  "men",
                  "premium",
                  "sports-footwear-sandals-flip-flops"
                ],
                "depth": 5,
                "children": []
              },
              {
                "label": "Backpacks",
                "value": "BGDE",
                "category_id": 6595,
                "url": [
                  "men",
                  "premium",
                  "sports-bags-backpacks-backpacks"
                ],
                "depth": 5,
                "children": []
              },
              {
                "label": "Messengers & Slings",
                "value": "BGDF",
                "category_id": 6594,
                "url": [
                  "men",
                  "premium",
                  "sports-bags-backpacks-messengers-slings"
                ],
                "depth": 5,
                "children": []
              },
              {
                "label": "Waistpouches",
                "value": "BGDG",
                "category_id": 6593,
                "url": [
                  "men",
                  "premium",
                  "sports-bags-backpacks-waistpouches"
                ],
                "depth": 5,
                "children": []
              },
              {
                "label": "Duffle Bags",
                "value": "BGDH",
                "category_id": 6591,
                "url": [
                  "men",
                  "premium",
                  "sports-bags-backpacks-duffle-bags"
                ],
                "depth": 5,
                "children": []
              },
              {
                "label": "Others",
                "value": "BGDI",
                "category_id": 6590,
                "url": [
                  "men",
                  "premium",
                  "sports-bags-backpacks-others"
                ],
                "depth": 5,
                "children": []
              },
              {
                "label": "Accessories",
                "value": "BGDJ",
                "category_id": 6506,
                "url": [
                  "men",
                  "premium",
                  "sports-accessories"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Training",
                "value": "BGDK",
                "category_id": 6505,
                "url": [
                  "men",
                  "premium",
                  "sports-training"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Running",
                "value": "BGDL",
                "category_id": 6504,
                "url": [
                  "men",
                  "premium",
                  "sports-running"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Swim & Beachwear",
                "value": "BGDM",
                "category_id": 6503,
                "url": [
                  "men",
                  "premium",
                  "sports-swim-beachwear"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Outdoors",
                "value": "BGDN",
                "category_id": 6502,
                "url": [
                  "men",
                  "premium",
                  "sports-outdoors"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Lifestyle",
                "value": "BGDO",
                "category_id": 6499,
                "url": [
                  "men",
                  "premium",
                  "sports-lifestyle"
                ],
                "depth": 4,
                "children": []
              }
            ]
          }
        ]
      }
    ]
  },
  {
    "label": "Women",
    "value": "A___",
    "category_id": 0,
    "url": [
      "women"
    ],
    "depth": 1,
    "children": [
      {
        "label": "Women's Clothing",
        "value": "AA__",
        "category_id": 3,
        "url": [
          "women",
          "clothing"
        ],
        "depth": 2,
        "children": []
      },
      {
        "label": "Women's Shoes",
        "value": "AB__",
        "category_id": 4,
        "url": [
          "women",
          "shoes"
        ],
        "depth": 2,
        "children": [
          {
            "label": "Heels",
            "value": "ABA_",
            "category_id": 8,
            "url": [
              "women",
              "shoes",
              "heels"
            ],
            "depth": 3,
            "children": [
              {
                "label": "Open Toes",
                "value": "ABAA",
                "category_id": 6741,
                "url": [
                  "women",
                  "shoes",
                  "open-toes-heels"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Low Heels",
                "value": "ABAB",
                "category_id": 2162,
                "url": [
                  "women",
                  "shoes",
                  "low-heels"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Mid Heels",
                "value": "ABAC",
                "category_id": 2161,
                "url": [
                  "women",
                  "shoes",
                  "mid-heels"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "High Heels",
                "value": "ABAD",
                "category_id": 661,
                "url": [
                  "women",
                  "shoes",
                  "high-heels"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Pumps",
                "value": "ABAE",
                "category_id": 383,
                "url": [
                  "women",
                  "shoes",
                  "pumps"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Sandals",
                "value": "ABAF",
                "category_id": 665,
                "url": [
                  "women",
                  "shoes",
                  "sandals-heels"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Platforms",
                "value": "ABAG",
                "category_id": 663,
                "url": [
                  "women",
                  "shoes",
                  "platforms"
                ],
                "depth": 4,
                "children": []
              }
            ]
          },
          {
            "label": "Boots",
            "value": "ABB_",
            "category_id": 15,
            "url": [
              "women",
              "shoes",
              "boots"
            ],
            "depth": 3,
            "children": [
              {
                "label": "Flat Boots",
                "value": "ABBA",
                "category_id": 6744,
                "url": [
                  "women",
                  "shoes",
                  "flat-boots"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Heeled Boots",
                "value": "ABBB",
                "category_id": 6743,
                "url": [
                  "women",
                  "shoes",
                  "heeled-boots"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Long Boots",
                "value": "ABBC",
                "category_id": 6742,
                "url": [
                  "women",
                  "shoes",
                  "long-boots"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Ankle Boots",
                "value": "ABBD",
                "category_id": 5,
                "url": [
                  "women",
                  "shoes",
                  "ankle-boots"
                ],
                "depth": 4,
                "children": []
              }
            ]
          },
          {
            "label": "Sneakers",
            "value": "ABC_",
            "category_id": 12,
            "url": [
              "women",
              "shoes",
              "sneakers"
            ],
            "depth": 3,
            "children": []
          },
          {
            "label": "Flats",
            "value": "ABD_",
            "category_id": 6,
            "url": [
              "women",
              "shoes",
              "flats"
            ],
            "depth": 3,
            "children": [
              {
                "label": "Oxford & Lace Up",
                "value": "ABDA",
                "category_id": 1779,
                "url": [
                  "women",
                  "shoes",
                  "oxford-lace-up"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Loafers & Boat Shoes",
                "value": "ABDB",
                "category_id": 1778,
                "url": [
                  "women",
                  "shoes",
                  "loafers-boat-shoes"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Espadrilles",
                "value": "ABDC",
                "category_id": 1588,
                "url": [
                  "women",
                  "shoes",
                  "espadrilles-flats"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Ballerinas",
                "value": "ABDD",
                "category_id": 390,
                "url": [
                  "women",
                  "shoes",
                  "ballerinas"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Peep Toes",
                "value": "ABDE",
                "category_id": 758,
                "url": [
                  "women",
                  "shoes",
                  "peep-toes-flats"
                ],
                "depth": 4,
                "children": []
              }
            ]
          },
          {
            "label": "Sandals",
            "value": "ABE_",
            "category_id": 386,
            "url": [
              "women",
              "shoes",
              "sandals"
            ],
            "depth": 3,
            "children": [
              {
                "label": "Espadrilles",
                "value": "ABEA",
                "category_id": 6766,
                "url": [
                  "women",
                  "shoes",
                  "espadrilles-sandals"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Flat Sandals",
                "value": "ABEB",
                "category_id": 666,
                "url": [
                  "women",
                  "shoes",
                  "flat-sandals"
                ],
                "depth": 4,
                "children": []
              }
            ]
          },
          {
            "label": "Wedges",
            "value": "ABF_",
            "category_id": 658,
            "url": [
              "women",
              "shoes",
              "wedges"
            ],
            "depth": 3,
            "children": [
              {
                "label": "Open Toes Wedges",
                "value": "ABFA",
                "category_id": 2165,
                "url": [
                  "women",
                  "shoes",
                  "open-toes-wedges"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Wedge Pumps",
                "value": "ABFB",
                "category_id": 2164,
                "url": [
                  "women",
                  "shoes",
                  "wedge-pumps"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Wedge Sandals",
                "value": "ABFC",
                "category_id": 2163,
                "url": [
                  "women",
                  "shoes",
                  "wedge-sandals"
                ],
                "depth": 4,
                "children": []
              }
            ]
          },
          {
            "label": "Slip-Ons",
            "value": "ABG_",
            "category_id": 2219,
            "url": [
              "women",
              "shoes",
              "slip-ons"
            ],
            "depth": 3,
            "children": []
          },
          {
            "label": "Flip Flops",
            "value": "ABH_",
            "category_id": 385,
            "url": [
              "women",
              "shoes",
              "flip-flops"
            ],
            "depth": 3,
            "children": []
          },
          {
            "label": "Sports Shoes",
            "value": "ABI_",
            "category_id": 394,
            "url": [
              "women",
              "shoes",
              "sports-shoes"
            ],
            "depth": 3,
            "children": []
          },
          {
            "label": "Comfort Shoes",
            "value": "ABJ_",
            "category_id": 391,
            "url": [
              "women",
              "shoes",
              "comfort-shoes"
            ],
            "depth": 3,
            "children": []
          }
        ]
      },
      {
        "label": "Women's Accessories",
        "value": "AC__",
        "category_id": 256,
        "url": [
          "women",
          "accessories"
        ],
        "depth": 2,
        "children": [
          {
            "label": "Watches",
            "value": "ACA_",
            "category_id": 3242,
            "url": [
              "women",
              "accessories",
              "watches"
            ],
            "depth": 3,
            "children": [
              {
                "label": "Analogue Watches",
                "value": "ACAA",
                "category_id": 3253,
                "url": [
                  "women",
                  "accessories",
                  "analogue-watches"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Digital Watches",
                "value": "ACAB",
                "category_id": 3252,
                "url": [
                  "women",
                  "accessories",
                  "digital-watches"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Sports Watches",
                "value": "ACAC",
                "category_id": 3251,
                "url": [
                  "women",
                  "accessories",
                  "sports-watches"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Fashion Watches",
                "value": "ACAD",
                "category_id": 3244,
                "url": [
                  "women",
                  "accessories",
                  "fashion-watches"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Casual Watches",
                "value": "ACAE",
                "category_id": 4830,
                "url": [
                  "women",
                  "accessories",
                  "casual-watches"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Luxury Watches",
                "value": "ACAF",
                "category_id": 4832,
                "url": [
                  "women",
                  "accessories",
                  "luxury-watches"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Chronograph Watches",
                "value": "ACAG",
                "category_id": 4825,
                "url": [
                  "women",
                  "accessories",
                  "chronograph-watches"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Smart Watches",
                "value": "ACAH",
                "category_id": 5783,
                "url": [
                  "women",
                  "accessories",
                  "smart-watches"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Shop by Strap",
                "value": "ACAI",
                "category_id": 4826,
                "url": [
                  "women",
                  "accessories",
                  "shop-by-strap"
                ],
                "depth": 4,
                "children": []
              }
            ]
          },
          {
            "label": "Eyewear",
            "value": "ACB_",
            "category_id": 6767,
            "url": [
              "women",
              "accessories",
              "eyewear"
            ],
            "depth": 3,
            "children": [
              {
                "label": "Sunglasses",
                "value": "ACBA",
                "category_id": 290,
                "url": [
                  "women",
                  "accessories",
                  "sunglasses"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Glasses",
                "value": "ACBB",
                "category_id": 4602,
                "url": [
                  "women",
                  "accessories",
                  "glasses"
                ],
                "depth": 4,
                "children": []
              }
            ]
          },
          {
            "label": "Jewellery",
            "value": "ACC_",
            "category_id": 259,
            "url": [
              "women",
              "accessories",
              "jewellery"
            ],
            "depth": 3,
            "children": [
              {
                "label": "Pendants",
                "value": "ACCA",
                "category_id": 6768,
                "url": [
                  "women",
                  "accessories",
                  "pendants"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Brooches",
                "value": "ACCB",
                "category_id": 4801,
                "url": [
                  "women",
                  "accessories",
                  "brooches"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Bracelets & Bangles",
                "value": "ACCC",
                "category_id": 975,
                "url": [
                  "women",
                  "accessories",
                  "bracelets-bangles"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Charms",
                "value": "ACCD",
                "category_id": 263,
                "url": [
                  "women",
                  "accessories",
                  "charms"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Rings",
                "value": "ACCE",
                "category_id": 262,
                "url": [
                  "women",
                  "accessories",
                  "rings"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Earrings",
                "value": "ACCF",
                "category_id": 261,
                "url": [
                  "women",
                  "accessories",
                  "earrings"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Necklaces",
                "value": "ACCG",
                "category_id": 258,
                "url": [
                  "women",
                  "accessories",
                  "necklaces"
                ],
                "depth": 4,
                "children": []
              }
            ]
          },
          {
            "label": "Scarves & Shawls",
            "value": "ACD_",
            "category_id": 403,
            "url": [
              "women",
              "accessories",
              "scarves-shawls"
            ],
            "depth": 3,
            "children": [
              {
                "label": "Scarves",
                "value": "ACDA",
                "category_id": 5365,
                "url": [
                  "women",
                  "accessories",
                  "scarves"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Hijabs",
                "value": "ACDB",
                "category_id": 5366,
                "url": [
                  "women",
                  "accessories",
                  "hijabs"
                ],
                "depth": 4,
                "children": []
              }
            ]
          },
          {
            "label": "Hair Accessories",
            "value": "ACE_",
            "category_id": 279,
            "url": [
              "women",
              "accessories",
              "hair-accessories"
            ],
            "depth": 3,
            "children": [
              {
                "label": "Hair Ties",
                "value": "ACEA",
                "category_id": 309,
                "url": [
                  "women",
                  "accessories",
                  "hair-ties"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Clips",
                "value": "ACEB",
                "category_id": 283,
                "url": [
                  "women",
                  "accessories",
                  "clips"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Bows",
                "value": "ACEC",
                "category_id": 282,
                "url": [
                  "women",
                  "accessories",
                  "bows"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Head Bands",
                "value": "ACED",
                "category_id": 280,
                "url": [
                  "women",
                  "accessories",
                  "head-bands"
                ],
                "depth": 4,
                "children": []
              }
            ]
          },
          {
            "label": "Technology",
            "value": "ACF_",
            "category_id": 299,
            "url": [
              "women",
              "accessories",
              "technology"
            ],
            "depth": 3,
            "children": [
              {
                "label": "Laptop Bags & Sleeves",
                "value": "ACFA",
                "category_id": 978,
                "url": [
                  "women",
                  "accessories",
                  "laptop-bags-sleeves"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Gadgets & Accessories",
                "value": "ACFB",
                "category_id": 6769,
                "url": [
                  "women",
                  "accessories",
                  "gadgets-accessories"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Phone & Tablet Cases",
                "value": "ACFC",
                "category_id": 301,
                "url": [
                  "women",
                  "accessories",
                  "phone-tablet-cases"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Headphones & Headsets",
                "value": "ACFD",
                "category_id": 300,
                "url": [
                  "women",
                  "accessories",
                  "headphones-headsets"
                ],
                "depth": 4,
                "children": []
              }
            ]
          },
          {
            "label": "Other Accessories",
            "value": "ACG_",
            "category_id": 406,
            "url": [
              "women",
              "accessories",
              "other-accessories"
            ],
            "depth": 3,
            "children": [
              {
                "label": "Stationery & Living",
                "value": "ACGA",
                "category_id": 6948,
                "url": [
                  "women",
                  "accessories",
                  "stationery-living"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Hats & Caps",
                "value": "ACGB",
                "category_id": 402,
                "url": [
                  "women",
                  "accessories",
                  "hats-caps"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Belts",
                "value": "ACGC",
                "category_id": 271,
                "url": [
                  "women",
                  "accessories",
                  "belts"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Gloves",
                "value": "ACGD",
                "category_id": 287,
                "url": [
                  "women",
                  "accessories",
                  "gloves"
                ],
                "depth": 4,
                "children": []
              }
            ]
          }
        ]
      },
      {
        "label": "Women's Bags",
        "value": "AD__",
        "category_id": 399,
        "url": [
          "women",
          "bags"
        ],
        "depth": 2,
        "children": [
          {
            "label": "Clutches",
            "value": "ADA_",
            "category_id": 784,
            "url": [
              "women",
              "bags",
              "clutches"
            ],
            "depth": 3,
            "children": []
          },
          {
            "label": "Crossbody Bags",
            "value": "ADB_",
            "category_id": 781,
            "url": [
              "women",
              "bags",
              "crossbody-bags"
            ],
            "depth": 3,
            "children": []
          },
          {
            "label": "Tote Bags",
            "value": "ADC_",
            "category_id": 780,
            "url": [
              "women",
              "bags",
              "tote-bags"
            ],
            "depth": 3,
            "children": []
          },
          {
            "label": "Wallets & Purses",
            "value": "ADD_",
            "category_id": 976,
            "url": [
              "women",
              "bags",
              "wallets-purses"
            ],
            "depth": 3,
            "children": [
              {
                "label": "Purses",
                "value": "ADDA",
                "category_id": 401,
                "url": [
                  "women",
                  "bags",
                  "purses"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Wallets",
                "value": "ADDB",
                "category_id": 977,
                "url": [
                  "women",
                  "bags",
                  "wallets"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Bag Accessories",
                "value": "ADDC",
                "category_id": 6765,
                "url": [
                  "women",
                  "bags",
                  "bag-accessories"
                ],
                "depth": 4,
                "children": []
              }
            ]
          },
          {
            "label": "Backpacks",
            "value": "ADE_",
            "category_id": 783,
            "url": [
              "women",
              "bags",
              "backpacks"
            ],
            "depth": 3,
            "children": []
          },
          {
            "label": "Leather Bags",
            "value": "ADF_",
            "category_id": 2221,
            "url": [
              "women",
              "bags",
              "leather-bags"
            ],
            "depth": 3,
            "children": []
          },
          {
            "label": "Travel",
            "value": "ADG_",
            "category_id": 990,
            "url": [
              "women",
              "bags",
              "travel"
            ],
            "depth": 3,
            "children": [
              {
                "label": "Hand Luggage",
                "value": "ADGA",
                "category_id": 2226,
                "url": [
                  "women",
                  "bags",
                  "hand-luggage"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Wheeled Luggage",
                "value": "ADGB",
                "category_id": 2225,
                "url": [
                  "women",
                  "bags",
                  "wheeled-luggage"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Travel Backpacks",
                "value": "ADGC",
                "category_id": 2224,
                "url": [
                  "women",
                  "bags",
                  "travel-backpacks"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Travel Accessories",
                "value": "ADGD",
                "category_id": 2223,
                "url": [
                  "women",
                  "bags",
                  "travel-accessories"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Belt Bags",
                "value": "ADGE",
                "category_id": 6763,
                "url": [
                  "women",
                  "bags",
                  "belt-bags"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Weekender",
                "value": "ADGF",
                "category_id": 6764,
                "url": [
                  "women",
                  "bags",
                  "weekender"
                ],
                "depth": 4,
                "children": []
              }
            ]
          },
          {
            "label": "Hand Bags",
            "value": "ADH_",
            "category_id": 6762,
            "url": [
              "women",
              "bags",
              "hand-bags"
            ],
            "depth": 3,
            "children": []
          },
          {
            "label": "Shopper Bags",
            "value": "ADI_",
            "category_id": 779,
            "url": [
              "women",
              "bags",
              "shopper-bags"
            ],
            "depth": 3,
            "children": []
          },
          {
            "label": "Laptop Bags",
            "value": "ADJ_",
            "category_id": 400,
            "url": [
              "women",
              "bags",
              "laptop-bags"
            ],
            "depth": 3,
            "children": []
          }
        ]
      },
      {
        "label": "Women's Sports",
        "value": "AE__",
        "category_id": 472,
        "url": [
          "women",
          "sports"
        ],
        "depth": 2,
        "children": [
          {
            "label": "Shop by Category",
            "value": "AEA_",
            "category_id": 6746,
            "url": [
              "women",
              "sports",
              "shop-by-category"
            ],
            "depth": 3,
            "children": [
              {
                "label": "Clothing",
                "value": "AEAA",
                "category_id": 469,
                "url": [
                  "women",
                  "sports",
                  "clothing"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Shoes",
                "value": "AEAB",
                "category_id": 555,
                "url": [
                  "women",
                  "sports",
                  "shoes"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Bags & Backpacks",
                "value": "AEAC",
                "category_id": 2241,
                "url": [
                  "women",
                  "sports",
                  "bags-backpacks"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Accessories",
                "value": "AEAD",
                "category_id": 556,
                "url": [
                  "women",
                  "sports",
                  "accessories"
                ],
                "depth": 4,
                "children": []
              }
            ]
          },
          {
            "label": "Shop by Sport Activity",
            "value": "AEB_",
            "category_id": 6745,
            "url": [
              "women",
              "sports",
              "shop-by-sport-activity"
            ],
            "depth": 3,
            "children": [
              {
                "label": "Training",
                "value": "AEBA",
                "category_id": 5800,
                "url": [
                  "women",
                  "sports",
                  "training"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Lifestyle",
                "value": "AEBB",
                "category_id": 5844,
                "url": [
                  "women",
                  "sports",
                  "lifestyle"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Running",
                "value": "AEBC",
                "category_id": 5811,
                "url": [
                  "women",
                  "sports",
                  "running"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Swimming & Surf",
                "value": "AEBD",
                "category_id": 5822,
                "url": [
                  "women",
                  "sports",
                  "swimming-surf"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Outdoors",
                "value": "AEBE",
                "category_id": 6820,
                "url": [
                  "women",
                  "sports",
                  "outdoors"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Yoga",
                "value": "AEBF",
                "category_id": 6841,
                "url": [
                  "women",
                  "sports",
                  "yoga"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Team Sports",
                "value": "AEBG",
                "category_id": 6816,
                "url": [
                  "women",
                  "sports",
                  "team-sports"
                ],
                "depth": 4,
                "children": []
              }
            ]
          }
        ]
      },
      {
        "label": "Women's Premium",
        "value": "AF__",
        "category_id": 5389,
        "url": [
          "women",
          "premium"
        ],
        "depth": 2,
        "children": [
          {
            "label": "Clothing",
            "value": "AFA_",
            "category_id": 5390,
            "url": [
              "women",
              "premium",
              "clothing"
            ],
            "depth": 3,
            "children": [
              {
                "label": "Dresses",
                "value": "AFAA",
                "category_id": 6129,
                "url": [
                  "women",
                  "premium",
                  "dresses"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Tops",
                "value": "AFAB",
                "category_id": 6146,
                "url": [
                  "women",
                  "premium",
                  "tops"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Skirts",
                "value": "AFAC",
                "category_id": 6145,
                "url": [
                  "women",
                  "premium",
                  "skirts"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Playsuits & Jumpsuits",
                "value": "AFAD",
                "category_id": 6144,
                "url": [
                  "women",
                  "premium",
                  "playsuits-jumpsuits"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Shorts",
                "value": "AFAE",
                "category_id": 6143,
                "url": [
                  "women",
                  "premium",
                  "shorts"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Pants & Leggings",
                "value": "AFAF",
                "category_id": 6142,
                "url": [
                  "women",
                  "premium",
                  "pants-leggings"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Swimwear & Beachwear",
                "value": "AFAG",
                "category_id": 6141,
                "url": [
                  "women",
                  "premium",
                  "swimwear-beachwear"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Jeans",
                "value": "AFAH",
                "category_id": 6140,
                "url": [
                  "women",
                  "premium",
                  "jeans"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Lingerie & Sleepwear",
                "value": "AFAI",
                "category_id": 6139,
                "url": [
                  "women",
                  "premium",
                  "lingerie-sleepwear"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Sleepwear",
                "value": "AFAJ",
                "category_id": 6138,
                "url": [
                  "women",
                  "premium",
                  "sleepwear"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Petite",
                "value": "AFAK",
                "category_id": 6137,
                "url": [
                  "women",
                  "premium",
                  "petite"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Knitwear & Cardigans",
                "value": "AFAL",
                "category_id": 6136,
                "url": [
                  "women",
                  "premium",
                  "knitwear-cardigans"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Hoodies & Sweatshirts",
                "value": "AFAM",
                "category_id": 6135,
                "url": [
                  "women",
                  "premium",
                  "hoodies-sweatshirts"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Blazers",
                "value": "AFAN",
                "category_id": 6134,
                "url": [
                  "women",
                  "premium",
                  "blazers"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Jackets & Coats",
                "value": "AFAO",
                "category_id": 6133,
                "url": [
                  "women",
                  "premium",
                  "jackets-coats"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Maternity",
                "value": "AFAP",
                "category_id": 6131,
                "url": [
                  "women",
                  "premium",
                  "maternity"
                ],
                "depth": 4,
                "children": []
              }
            ]
          },
          {
            "label": "Shoes",
            "value": "AFB_",
            "category_id": 5391,
            "url": [
              "women",
              "premium",
              "shoes"
            ],
            "depth": 3,
            "children": [
              {
                "label": "Flats",
                "value": "AFBA",
                "category_id": 6156,
                "url": [
                  "women",
                  "premium",
                  "flats"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Heels",
                "value": "AFBB",
                "category_id": 6155,
                "url": [
                  "women",
                  "premium",
                  "heels"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Sandals",
                "value": "AFBC",
                "category_id": 6154,
                "url": [
                  "women",
                  "premium",
                  "sandals"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Wedges",
                "value": "AFBD",
                "category_id": 6153,
                "url": [
                  "women",
                  "premium",
                  "wedges"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Slip-Ons",
                "value": "AFBE",
                "category_id": 6152,
                "url": [
                  "women",
                  "premium",
                  "slip-ons"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Boots",
                "value": "AFBF",
                "category_id": 6151,
                "url": [
                  "women",
                  "premium",
                  "boots"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Sneakers",
                "value": "AFBG",
                "category_id": 6150,
                "url": [
                  "women",
                  "premium",
                  "sneakers"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Flip Flops",
                "value": "AFBH",
                "category_id": 6149,
                "url": [
                  "women",
                  "premium",
                  "flip-flops"
                ],
                "depth": 4,
                "children": []
              }
            ]
          },
          {
            "label": "Accessories",
            "value": "AFC_",
            "category_id": 5392,
            "url": [
              "women",
              "premium",
              "accessories"
            ],
            "depth": 3,
            "children": [
              {
                "label": "Bags & Purses",
                "value": "AFCA",
                "category_id": 6163,
                "url": [
                  "women",
                  "premium",
                  "bags-purses"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Watches",
                "value": "AFCB",
                "category_id": 6162,
                "url": [
                  "women",
                  "premium",
                  "watches"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Travel",
                "value": "AFCC",
                "category_id": 6161,
                "url": [
                  "women",
                  "premium",
                  "travel"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Eyewear",
                "value": "AFCD",
                "category_id": 6160,
                "url": [
                  "women",
                  "premium",
                  "eyewear"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Jewellery",
                "value": "AFCE",
                "category_id": 6159,
                "url": [
                  "women",
                  "premium",
                  "jewellery"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Scarves & Shawls",
                "value": "AFCF",
                "category_id": 6158,
                "url": [
                  "women",
                  "premium",
                  "scarves-shawls"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Others",
                "value": "AFCG",
                "category_id": 6157,
                "url": [
                  "women",
                  "premium",
                  "other-accessories"
                ],
                "depth": 4,
                "children": []
              }
            ]
          },
          {
            "label": "Sports",
            "value": "AFD_",
            "category_id": 5986,
            "url": [
              "women",
              "premium",
              "sports"
            ],
            "depth": 3,
            "children": [
              {
                "label": "Clothing",
                "value": "AFDA",
                "category_id": 6175,
                "url": [
                  "women",
                  "premium",
                  "sports-clothing"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Shoes",
                "value": "AFDB",
                "category_id": 6174,
                "url": [
                  "women",
                  "premium",
                  "shoes"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Bags & Backpacks",
                "value": "AFDC",
                "category_id": 6173,
                "url": [
                  "women",
                  "premium",
                  "sports-bags-backpacks"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Accessories",
                "value": "AFDD",
                "category_id": 6172,
                "url": [
                  "women",
                  "premium",
                  "sports-accessories"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Training",
                "value": "AFDE",
                "category_id": 6171,
                "url": [
                  "women",
                  "premium",
                  "sports-training"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Running",
                "value": "AFDF",
                "category_id": 6170,
                "url": [
                  "women",
                  "premium",
                  "sports-running"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Swim & Beachwear",
                "value": "AFDG",
                "category_id": 6169,
                "url": [
                  "women",
                  "premium",
                  "sports-swim-beachwear"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Outdoors",
                "value": "AFDH",
                "category_id": 6168,
                "url": [
                  "women",
                  "premium",
                  "sports-outdoors"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Boxing & MMA",
                "value": "AFDI",
                "category_id": 6167,
                "url": [
                  "women",
                  "premium",
                  "sports-boxing-mma"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Lifestyle",
                "value": "AFDJ",
                "category_id": 6166,
                "url": [
                  "women",
                  "premium",
                  "sports-lifestyle"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Yoga",
                "value": "AFDK",
                "category_id": 6165,
                "url": [
                  "women",
                  "premium",
                  "sports-yoga"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Others",
                "value": "AFDL",
                "category_id": 6164,
                "url": [
                  "women",
                  "premium",
                  "sports-others"
                ],
                "depth": 4,
                "children": []
              }
            ]
          },
          {
            "label": "Beauty",
            "value": "AFE_",
            "category_id": 5985,
            "url": [
              "women",
              "premium",
              "beauty"
            ],
            "depth": 3,
            "children": [
              {
                "label": "Hair",
                "value": "AFEA",
                "category_id": 6179,
                "url": [
                  "women",
                  "premium",
                  "hair"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Tools & Brushes",
                "value": "AFEB",
                "category_id": 6178,
                "url": [
                  "women",
                  "premium",
                  "tools-brushes"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Palettes & Sets",
                "value": "AFEC",
                "category_id": 6177,
                "url": [
                  "women",
                  "premium",
                  "palettes-sets"
                ],
                "depth": 4,
                "children": []
              }
            ]
          }
        ]
      },
      {
        "label": "Women's Beauty",
        "value": "AG__",
        "category_id": 5480,
        "url": [
          "women",
          "beauty"
        ],
        "depth": 2,
        "children": [
          {
            "label": "Makeup",
            "value": "AGA_",
            "category_id": 5521,
            "url": [
              "women",
              "beauty",
              "makeup"
            ],
            "depth": 3,
            "children": [
              {
                "label": "Face",
                "value": "AGAA",
                "category_id": 5535,
                "url": [
                  "women",
                  "beauty",
                  "face"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Eyes",
                "value": "AGAB",
                "category_id": 5527,
                "url": [
                  "women",
                  "beauty",
                  "eyes"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Lips",
                "value": "AGAC",
                "category_id": 5522,
                "url": [
                  "women",
                  "beauty",
                  "lips"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Palettes & Sets",
                "value": "AGAD",
                "category_id": 5487,
                "url": [
                  "women",
                  "beauty",
                  "makeup-palettes-sets"
                ],
                "depth": 4,
                "children": []
              }
            ]
          },
          {
            "label": "Skin Care",
            "value": "AGB_",
            "category_id": 5506,
            "url": [
              "women",
              "beauty",
              "skin-care"
            ],
            "depth": 3,
            "children": [
              {
                "label": "Cleanse",
                "value": "AGBA",
                "category_id": 5517,
                "url": [
                  "women",
                  "beauty",
                  "cleanse"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Moisturize",
                "value": "AGBB",
                "category_id": 5513,
                "url": [
                  "women",
                  "beauty",
                  "moisturize"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Treatments",
                "value": "AGBC",
                "category_id": 5507,
                "url": [
                  "women",
                  "beauty",
                  "skin-care-treatments"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Dermacare",
                "value": "AGBD",
                "category_id": 6709,
                "url": [
                  "women",
                  "beauty",
                  "dermacare"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Sun Care",
                "value": "AGBE",
                "category_id": 5514,
                "url": [
                  "women",
                  "beauty",
                  "sun-care"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Palettes & Sets",
                "value": "AGBF",
                "category_id": 5486,
                "url": [
                  "women",
                  "beauty",
                  "skin-care-palettes-sets"
                ],
                "depth": 4,
                "children": []
              }
            ]
          },
          {
            "label": "Body",
            "value": "AGC_",
            "category_id": 5501,
            "url": [
              "women",
              "beauty",
              "body"
            ],
            "depth": 3,
            "children": [
              {
                "label": "Body Washes & Exfoliators",
                "value": "AGCA",
                "category_id": 5505,
                "url": [
                  "women",
                  "beauty",
                  "body-washes-exfoliators"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Body Lotion",
                "value": "AGCB",
                "category_id": 5504,
                "url": [
                  "women",
                  "beauty",
                  "body-lotion"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Hand & Foot Care",
                "value": "AGCC",
                "category_id": 5503,
                "url": [
                  "women",
                  "beauty",
                  "hand-foot-care"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Treatments",
                "value": "AGCD",
                "category_id": 5502,
                "url": [
                  "women",
                  "beauty",
                  "body-treatments"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Palettes & Sets",
                "value": "AGCE",
                "category_id": 5485,
                "url": [
                  "women",
                  "beauty",
                  "body-palettes-sets"
                ],
                "depth": 4,
                "children": []
              }
            ]
          },
          {
            "label": "Nails",
            "value": "AGD_",
            "category_id": 5497,
            "url": [
              "women",
              "beauty",
              "nails"
            ],
            "depth": 3,
            "children": [
              {
                "label": "Nail Polish",
                "value": "AGDA",
                "category_id": 5500,
                "url": [
                  "women",
                  "beauty",
                  "nail-polish"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Nail Effects",
                "value": "AGDB",
                "category_id": 5499,
                "url": [
                  "women",
                  "beauty",
                  "nail-effects"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Nail Care & Tools",
                "value": "AGDC",
                "category_id": 5498,
                "url": [
                  "women",
                  "beauty",
                  "nail-care-tools"
                ],
                "depth": 4,
                "children": []
              }
            ]
          },
          {
            "label": "Hair",
            "value": "AGE_",
            "category_id": 5493,
            "url": [
              "women",
              "beauty",
              "hair"
            ],
            "depth": 3,
            "children": [
              {
                "label": "Shampoo & Conditioners",
                "value": "AGEA",
                "category_id": 5496,
                "url": [
                  "women",
                  "beauty",
                  "shampoo-conditioners"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Hair Masks & Treatments",
                "value": "AGEB",
                "category_id": 5495,
                "url": [
                  "women",
                  "beauty",
                  "hair-masks-treatments"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Styling",
                "value": "AGEC",
                "category_id": 5494,
                "url": [
                  "women",
                  "beauty",
                  "styling"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Palettes & Sets",
                "value": "AGED",
                "category_id": 5484,
                "url": [
                  "women",
                  "beauty",
                  "hair-palettes-sets"
                ],
                "depth": 4,
                "children": []
              }
            ]
          },
          {
            "label": "Tools & Brushes",
            "value": "AGF_",
            "category_id": 5488,
            "url": [
              "women",
              "beauty",
              "tools-brushes"
            ],
            "depth": 3,
            "children": [
              {
                "label": "Brushes",
                "value": "AGFA",
                "category_id": 6770,
                "url": [
                  "women",
                  "beauty",
                  "brushes"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Tools",
                "value": "AGFB",
                "category_id": 6771,
                "url": [
                  "women",
                  "beauty",
                  "tools"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Makeup Bags & Cases",
                "value": "AGFC",
                "category_id": 5489,
                "url": [
                  "women",
                  "beauty",
                  "makeup-bags-cases"
                ],
                "depth": 4,
                "children": []
              }
            ]
          },
          {
            "label": "Fragrance",
            "value": "AGG_",
            "category_id": 5482,
            "url": [
              "women",
              "beauty",
              "fragrance"
            ],
            "depth": 3,
            "children": []
          }
        ]
      },
      {
        "label": "Women's Trends",
        "value": "AH__",
        "category_id": 5996,
        "url": [
          "women",
          "trends"
        ],
        "depth": 2,
        "children": [
          {
            "label": "Florals",
            "value": "AHA_",
            "category_id": 5998,
            "url": [
              "women",
              "trends",
              "florals"
            ],
            "depth": 3,
            "children": [
              {
                "label": "Clothing",
                "value": "AHAA",
                "category_id": 6023,
                "url": [
                  "women",
                  "trends",
                  "florals-clothing"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Shoes",
                "value": "AHAB",
                "category_id": 6022,
                "url": [
                  "women",
                  "trends",
                  "florals-shoes"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Accessories",
                "value": "AHAC",
                "category_id": 6021,
                "url": [
                  "women",
                  "trends",
                  "florals-accessories"
                ],
                "depth": 4,
                "children": []
              }
            ]
          },
          {
            "label": "Nude and Neutrals",
            "value": "AHB_",
            "category_id": 5999,
            "url": [
              "women",
              "trends",
              "nude-neutrals"
            ],
            "depth": 3,
            "children": [
              {
                "label": "Clothing",
                "value": "AHBA",
                "category_id": 6026,
                "url": [
                  "women",
                  "trends",
                  "nude-neutrals-clothing"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Shoes",
                "value": "AHBB",
                "category_id": 6025,
                "url": [
                  "women",
                  "trends",
                  "nude-neutrals-shoes"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Accessories",
                "value": "AHBC",
                "category_id": 6024,
                "url": [
                  "women",
                  "trends",
                  "nude-neutrals-accessories"
                ],
                "depth": 4,
                "children": []
              }
            ]
          },
          {
            "label": "Denim",
            "value": "AHC_",
            "category_id": 6000,
            "url": [
              "women",
              "trends",
              "denim"
            ],
            "depth": 3,
            "children": [
              {
                "label": "Clothing",
                "value": "AHCA",
                "category_id": 6029,
                "url": [
                  "women",
                  "trends",
                  "denim-clothing"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Accessories",
                "value": "AHCB",
                "category_id": 6027,
                "url": [
                  "women",
                  "trends",
                  "denim-accessories"
                ],
                "depth": 4,
                "children": []
              }
            ]
          },
          {
            "label": "Monochrome",
            "value": "AHD_",
            "category_id": 6001,
            "url": [
              "women",
              "trends",
              "monochrome"
            ],
            "depth": 3,
            "children": [
              {
                "label": "Clothing",
                "value": "AHDA",
                "category_id": 6032,
                "url": [
                  "women",
                  "trends",
                  "monochrome-clothing"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Shoes",
                "value": "AHDB",
                "category_id": 6031,
                "url": [
                  "women",
                  "trends",
                  "monochrome-shoes"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Accessories",
                "value": "AHDC",
                "category_id": 6030,
                "url": [
                  "women",
                  "trends",
                  "monochrome-accessories"
                ],
                "depth": 4,
                "children": []
              }
            ]
          },
          {
            "label": "Athleisure",
            "value": "AHE_",
            "category_id": 6002,
            "url": [
              "women",
              "trends",
              "athleisure"
            ],
            "depth": 3,
            "children": [
              {
                "label": "Clothing",
                "value": "AHEA",
                "category_id": 6035,
                "url": [
                  "women",
                  "trends",
                  "athleisure-clothing"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Shoes",
                "value": "AHEB",
                "category_id": 6034,
                "url": [
                  "women",
                  "trends",
                  "athleisure-shoes"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Accessories",
                "value": "AHEC",
                "category_id": 6033,
                "url": [
                  "women",
                  "trends",
                  "athleisure-accessories"
                ],
                "depth": 4,
                "children": []
              }
            ]
          },
          {
            "label": "Lace",
            "value": "AHF_",
            "category_id": 6003,
            "url": [
              "women",
              "trends",
              "lace"
            ],
            "depth": 3,
            "children": [
              {
                "label": "Clothing",
                "value": "AHFA",
                "category_id": 6038,
                "url": [
                  "women",
                  "trends",
                  "lace-clothing"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Shoes",
                "value": "AHFB",
                "category_id": 6037,
                "url": [
                  "women",
                  "trends",
                  "lace-shoes"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Accessories",
                "value": "AHFC",
                "category_id": 6036,
                "url": [
                  "women",
                  "trends",
                  "lace-accessories"
                ],
                "depth": 4,
                "children": []
              }
            ]
          },
          {
            "label": "Stripes",
            "value": "AHG_",
            "category_id": 6004,
            "url": [
              "women",
              "trends",
              "stripes"
            ],
            "depth": 3,
            "children": [
              {
                "label": "Clothing",
                "value": "AHGA",
                "category_id": 6041,
                "url": [
                  "women",
                  "trends",
                  "stripes-clothing"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Shoes",
                "value": "AHGB",
                "category_id": 6040,
                "url": [
                  "women",
                  "trends",
                  "stripes-shoes"
                ],
                "depth": 4,
                "children": []
              },
              {
                "label": "Accessories",
                "value": "AHGC",
                "category_id": 6039,
                "url": [
                  "women",
                  "trends",
                  "stripes-accessories"
                ],
                "depth": 4,
                "children": []
              }
            ]
          }
        ]
      }
    ]
  }
]
url_cate_list = []


def category_browser(children):
    for child in children:
        if child['children']:
            category_browser(child['children'])
        url = construct_url(child['category_id'], child['url'][0])
        url_cate_list.append({
            "value": child['value'],
            "url": url
        })


class ProductSpider(scrapy.Spider):
    name = 'product'

    def start_requests(self):
        category_browser(data)
        for url_cate in url_cate_list:
            yield scrapy.Request(url=url_cate['url'], callback=self.parse, meta={'category': url_cate['value']})
            time.sleep(1)
        # yield scrapy.Request(url=url_cate_list[0]['url'], callback=self.parse, meta={'category': url_cate_list[0]['value']})

    def parse(self, response):
        file_obj = open('./data/product.sql', 'a', encoding='utf-8')
        category = response.meta['category']
        response = json.loads(response.body_as_unicode())
        for doc in response['response']['docs']:
            name = doc['meta']['name'].replace('"', ' inch')
            price = doc['meta']['price'].replace('HK$ ', '').replace(',', '')
            thumbnail_location = doc['image']
            insert_statement = 'INSERT INTO product (name, category, price, out_of_stock, thumbnail_location) VALUES ("'
            value = name + '", "' + category + '", ' + price + ', 0, "' + thumbnail_location + '");\n'
            insert_statement += value
            file_obj.write(insert_statement)

        file_obj.close()
