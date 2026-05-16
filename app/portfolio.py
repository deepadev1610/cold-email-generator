import pandas as pd
import chromadb
import uuid
from io import StringIO


class Portfolio:
    def __init__(
        self, file_path="app/resources/portfolios.xlsx", collection_name="portfolio"
    ):
        self.file_path = file_path
        self.collection_name = collection_name
        self.data = None
        self.chroma_client = chromadb.PersistentClient("vectorstore")
        self.collection = self.chroma_client.get_or_create_collection(
            name=self.collection_name
        )

        # Load default file if it exists
        try:
            self.data = pd.read_excel(self.file_path)
        except FileNotFoundError:
            self.data = pd.DataFrame(columns=["TechStack", "Links"])

    def load_portfolio_from_dataframe(self, dataframe):
        """Load portfolio data from a pandas DataFrame"""
        self.data = dataframe
        # Clear existing data in collection
        self._clear_collection()
        # Load new data
        self._add_data_to_collection()

    def load_portfolio_from_csv(self, csv_file):
        """Load portfolio data from an uploaded CSV file"""
        try:
            if isinstance(csv_file, str):
                # If it's a file path
                self.data = pd.read_csv(csv_file)
            else:
                # If it's a file object from Streamlit
                self.data = pd.read_csv(csv_file)

            # Clear existing data and load new
            self._clear_collection()
            self._add_data_to_collection()
            return True
        except Exception as e:
            print(f"Error loading CSV: {e}")
            return False

    def load_portfolio(self):
        """Load portfolio data from default file"""
        if self.data is not None and not self.data.empty:
            if self.collection.count() == 0:
                self._add_data_to_collection()

    def _add_data_to_collection(self):
        """Add data from self.data to ChromaDB collection"""
        if self.data is not None and not self.data.empty:
            for _, row in self.data.iterrows():
                try:
                    self.collection.add(
                        documents=str(row.get("TechStack", "")).strip(),
                        metadatas={"links": str(row.get("Links", "")).strip()},
                        ids=[str(uuid.uuid4())],
                    )
                except Exception as e:
                    print(f"Error adding row to collection: {e}")
                    continue

    def _clear_collection(self):
        """Clear all data from the collection"""
        try:
            # Delete and recreate collection
            self.chroma_client.delete_collection(name=self.collection_name)
            self.collection = self.chroma_client.get_or_create_collection(
                name=self.collection_name
            )
        except Exception as e:
            print(f"Error clearing collection: {e}")

    def query_link(self, skills):
        """Query portfolio links based on skills"""
        try:
            results = self.collection.query(query_texts=skills, n_results=2)
            return results.get("metadatas", [])
        except Exception as e:
            print(f"Error querying links: {e}")
            return []

    def get_portfolio_data(self):
        """Return current portfolio data"""
        return self.data
