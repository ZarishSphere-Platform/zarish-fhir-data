package sheets

import (
	"encoding/csv"
	"fmt"
	"os"
	"path/filepath"
)

type Exporter struct {
	OutputDir string
}

func NewExporter(outputDir string) *Exporter {
	return &Exporter{OutputDir: outputDir}
}

func (e *Exporter) Export(filename string, headers []string, data [][]string) error {
	filePath := filepath.Join(e.OutputDir, filename+".csv")
	file, err := os.Create(filePath)
	if err != nil {
		return fmt.Errorf("failed to create file: %w", err)
	}
	defer file.Close()

	writer := csv.NewWriter(file)
	defer writer.Flush()

	// Write Headers
	if err := writer.Write(headers); err != nil {
		return fmt.Errorf("failed to write headers: %w", err)
	}

	// Write Data
	if err := writer.WriteAll(data); err != nil {
		return fmt.Errorf("failed to write data: %w", err)
	}

	return nil
}
