import asyncio
from src.database.manager import DatabaseManager

async def test_database():
    print("Testing database setup...")
    db_manager = DatabaseManager()
    
    # Check files exist
    file_status = db_manager.list_available_files()
    for filename, exists in file_status.items():
        status = "✅" if exists else "❌"
        print(f"  {status} {filename}")
    
    # Initialize database
    await db_manager.initialize()
    print("✅ Database setup successful!")
    await db_manager.close()

if __name__ == "__main__":
    asyncio.run(test_database())
