# Facebook Marketplace Agent - Professional Edition

🚀 **Advanced automation agent for Facebook Marketplace with professional-grade modules and human-like behavior simulation.**

## 🌟 Professional Upgrade Features

### ✨ What's New in Professional Edition

- **🔧 Modular Architecture**: Complete restructure with professional automation modules
- **🤖 Advanced Anti-Detection**: Human behavior simulation with Bézier mouse movements
- **🛡️ Robust Error Recovery**: Professional error handling and recovery mechanisms  
- **📱 Smart Form Filling**: Intelligent form detection and adaptive filling strategies
- **🖼️ Advanced Image Handling**: Automatic image filtering and optimization
- **⚡ Performance Optimized**: Faster navigation with speed mode and caching
- **🔐 Enhanced Security**: Professional login system with advanced techniques

### 🏗️ New Module Structure

```
app/
├── core/
│   ├── automation/           # 🆕 Professional automation modules
│   │   ├── facebook/         # Facebook-specific automation
│   │   │   ├── marketplace.py    # Marketplace navigation
│   │   │   ├── housing.py        # Property form handling  
│   │   │   ├── item.py           # Item form handling
│   │   │   └── common.py         # Common form utilities
│   │   └── playwright/       # Playwright utilities
│   │       ├── nav.py            # Navigation helpers
│   │       ├── dom.py            # DOM interaction
│   │       └── ctx.py            # Context management
│   ├── facebook_marketplace_agent.py  # 🔄 Upgraded main agent
│   ├── stealth_browser.py
│   └── human_behavior.py
├── integrations/
│   └── facebook/
│       └── login.py          # 🔄 Enhanced login system
└── utils/                    # 🆕 Professional utilities
    ├── files.py              # File operations
    ├── images.py             # Image processing
    ├── text.py               # Text utilities
    ├── regex.py              # Regex patterns
    ├── money.py              # Money formatting
    └── clipboard.py          # Clipboard operations
```

## 🚀 Quick Start

### Prerequisites

```bash
pip install playwright beautifulsoup4 pillow
playwright install chromium
```

### Basic Usage

#### 1. Property Listing (Simplified)

```python
import asyncio
from pathlib import Path
from app.core.facebook_marketplace_agent import create_property_listing

async def create_rental():
    property_data = {
        'titulo': 'Casa Moderna en Renta',
        'descripcion': 'Hermosa casa con 3 recámaras en zona residencial',
        'precio': '25000',
        'recamaras': '3',
        'banos': '2',
        'direccion': 'Colonia Centro, Ensenada, BC'
    }
    
    # Optional: Add images folder
    images_folder = Path("./property_images")
    
    success = await create_property_listing(
        property_data,
        images_folder=images_folder,
        headless=False,  # Set to True for production
        listing_kind="Alquiler",
        fill_all_fields=True
    )
    
    print(f"Listing created: {success}")

asyncio.run(create_rental())
```

#### 2. Item Listing (Simplified)

```python
import asyncio
from app.core.facebook_marketplace_agent import create_item_listing

async def create_item():
    item_data = {
        'titulo': 'iPhone 13 Pro Max - Como Nuevo',
        'descripcion': 'iPhone en excelente estado con accesorios',
        'precio': '18000',
        'marca': 'Apple',
        'estado': 'Como nuevo'
    }
    
    success = await create_item_listing(
        item_data,
        headless=False,
        category_text="Teléfonos",
        condition_text="Como nuevo"
    )
    
    print(f"Item listed: {success}")

asyncio.run(create_item())
```

### Advanced Usage

#### Professional Agent with Full Control

```python
import asyncio
from pathlib import Path
from app.core.facebook_marketplace_agent import FacebookMarketplaceAgentPro

async def advanced_listing():
    async with FacebookMarketplaceAgentPro(headless=False) as agent:
        # Navigate to marketplace
        await agent.navigate_to_marketplace()
        
        # Create housing listing with full options
        property_data = {
            'titulo': 'Casa Familiar en Venta',
            'descripcion': 'Casa con acabados de lujo...',
            'precio': '2500000',
            'recamaras': '4',
            'banos': '3',
            'estacionamiento': '2',
            'area': '200'
        }
        
        images_folder = Path("./images")
        
        success = await agent.create_housing_listing(
            property_data,
            images_folder=images_folder,
            listing_kind="Venta",  # Sale
            property_type="Casa",
            fill_all_fields=True,
            upload_images=True
        )
        
        print(f"Advanced listing: {success}")

asyncio.run(advanced_listing())
```

## 🧪 Testing

### Run Complete Test Suite

```bash
cd facebook-marketplace-agent
python scripts/test_professional_agent.py
```

### Test Options

1. **Interactive Menu**: Choose specific tests
2. **Complete Workflow**: Run all tests automatically

### Test Coverage

- ✅ Agent initialization
- ✅ Marketplace navigation  
- ✅ Property listing creation
- ✅ Item listing creation
- ✅ Error recovery
- ✅ Human behavior simulation

## 📋 Property Data Format

### Required Fields

```python
property_data = {
    'titulo': 'Property Title',           # Required
    'descripcion': 'Property description' # Required
}
```

### Optional Fields

```python
property_data = {
    # Pricing
    'precio': '25000',                    # Price
    
    # Property details
    'recamaras': '3',                     # Bedrooms
    'banos': '2',                         # Bathrooms  
    'estacionamiento': '2',               # Parking spaces
    'area': '150',                        # Area in m²
    
    # Location
    'direccion': 'Full address',          # Address
    
    # Contact
    'contacto': '646-123-4567',           # Contact info
    
    # Property type
    'tipo': 'Casa',                       # Property type
    'subtipo': 'Casa habitación'          # Property subtype
}
```

## 📦 Item Data Format

### Required Fields

```python
item_data = {
    'titulo': 'Item Title',               # Required
    'descripcion': 'Item description'     # Required
}
```

### Optional Fields

```python
item_data = {
    # Pricing
    'precio': '5000',                     # Price
    
    # Item details
    'marca': 'Apple',                     # Brand
    'modelo': 'iPhone 13',                # Model
    'estado': 'Como nuevo',               # Condition
    
    # Contact
    'contacto': '646-987-6543'            # Contact info
}
```

## 🖼️ Image Management

### Automatic Image Processing

- **Auto-filtering**: Removes logos, maps, and promotional images
- **Natural sorting**: Orders images logically (1.jpg, 2.jpg, 10.jpg)
- **Size limits**: Respects Facebook limits (50 for properties, 10 for items)
- **Format support**: JPG, PNG, WebP

### Image Folder Structure

```
property_images/
├── 01_exterior.jpg
├── 02_living_room.jpg
├── 03_kitchen.jpg
├── 04_bedroom_1.jpg
└── ...
```

## 🔧 Configuration Options

### Agent Settings

```python
agent = FacebookMarketplaceAgentPro(
    headless=True,                    # Run without browser UI
    behavior_profile='normal'         # Behavior simulation level
)
```

### Listing Options

#### For Properties

```python
await agent.create_housing_listing(
    property_data,
    listing_kind="Alquiler",          # "Venta" or "Alquiler"
    property_type="Casa",             # Property type
    location_hint="City, State",      # Location fallback
    fill_all_fields=True,             # Fill optional fields
    upload_images=True                # Upload images
)
```

#### For Items

```python
await agent.create_item_listing(
    item_data,
    category_text="Varios",           # Item category
    condition_text="Nuevo",           # Item condition
    fill_all_fields=True,             # Fill optional fields
    upload_images=True                # Upload images
)
```

## 🛡️ Security & Anti-Detection

### Human Behavior Simulation

- **Natural typing**: Variable speed with realistic errors
- **Mouse movements**: Bézier curves for natural motion
- **Timing variations**: Random delays between actions
- **Error simulation**: Occasional typos and corrections

### Browser Stealth

- **User agent rotation**: Realistic browser signatures
- **Persistent profiles**: Maintains session data
- **Anti-detection flags**: Disables automation indicators
- **Viewport variation**: Random but realistic screen sizes

## 🔍 Debugging

### Debug Screenshots

The agent automatically takes screenshots for debugging:

- `debug_login_page.png` - Login page state
- `debug_login_failed.png` - Login failure state  
- `debug_login_error.png` - Login error state

### Logging

Enable detailed logging:

```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

## 📈 Performance Tips

### Speed Optimization

1. **Use headless mode** in production:
   ```python
   agent = FacebookMarketplaceAgentPro(headless=True)
   ```

2. **Enable speed mode** for navigation:
   ```python
   from app.core.automation.playwright import speed_mode
   async with speed_mode(context):
       # Fast navigation code
   ```

3. **Batch operations** when possible:
   ```python
   # Process multiple listings in one session
   async with FacebookMarketplaceAgentPro() as agent:
       for property_data in properties:
           await agent.create_housing_listing(property_data)
   ```

### Memory Management

- **Use context managers** to ensure cleanup
- **Close browsers** properly after use
- **Limit concurrent operations** to avoid memory issues

## 🚨 Important Notes

### Safety Features

- **Manual review required**: Agent prepares listings but doesn't auto-publish
- **Rate limiting**: Built-in delays to avoid detection
- **Error recovery**: Automatic recovery from common errors
- **Session persistence**: Maintains login across runs

### Best Practices

1. **Test thoroughly** before production use
2. **Use realistic data** to avoid suspicion
3. **Monitor for changes** in Facebook's interface
4. **Respect rate limits** and terms of service
5. **Keep credentials secure** (never hardcode)

## 🆘 Troubleshooting

### Common Issues

#### Login Problems
```python
# Clear cookies and retry
import os
if os.path.exists("facebook_cookies.json"):
    os.remove("facebook_cookies.json")
```

#### Form Filling Issues
```python
# Enable debug mode
await agent.create_housing_listing(
    property_data,
    fill_all_fields=False  # Try with minimal fields first
)
```

#### Navigation Issues
```python
# Use recovery navigation
await agent.recovery_navigation()
```

### Getting Help

1. **Check logs** for detailed error messages
2. **Review screenshots** in debug mode
3. **Test with simplified data** first
4. **Verify Facebook hasn't changed** interface elements

## 📜 License

This project is for educational and research purposes. Please ensure compliance with Facebook's Terms of Service and applicable laws.

## 🤝 Contributing

We welcome contributions! Please:

1. Fork the repository
2. Create a feature branch
3. Add tests for new functionality
4. Submit a pull request

---

**Professional Facebook Marketplace Agent v2.0** - Built with ❤️ for reliable automation