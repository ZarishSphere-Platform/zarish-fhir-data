package main

import (
	"flag"
	"log"
	"os"

	"github.com/zarishsphere-platform/zarish-fhir-data/pkg/sheets"
)

func main() {
	outputDir := flag.String("output", "./exports", "Output directory for CSV files")
	flag.Parse()

	if err := os.MkdirAll(*outputDir, 0755); err != nil {
		log.Fatalf("Failed to create output directory: %v", err)
	}

	exporter := sheets.NewExporter(*outputDir)
	
	// Example export (in a real scenario, this would fetch from DB or API)
	err := exporter.Export("patients", []string{"ID", "Name", "Gender", "BirthDate"}, [][]string{
		{"1", "John Doe", "male", "1980-01-01"},
		{"2", "Jane Smith", "female", "1990-05-15"},
	})

	if err != nil {
		log.Fatalf("Export failed: %v", err)
	}

	log.Printf("Export completed successfully to %s", *outputDir)
}
